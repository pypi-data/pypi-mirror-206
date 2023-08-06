# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import base64
import json
import logging
import os
from pathlib import Path
import requests
import tenacity
import time
from typing import Optional
import yaml

from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import SearchIndex, SimpleField, SearchableField, SemanticSettings, SemanticConfiguration, PrioritizedFields, SemanticField, SearchField, ComplexField
from azure.search.documents import SearchClient

from azureml.rag.embeddings import Embeddings
from azureml.rag.utils.azureml import get_secret_from_workspace
from azureml.rag.utils.logging import get_logger, enable_stdout_logging


logger = get_logger('update_acs')

_azure_logger = logging.getLogger('azure.core.pipeline')
_azure_logger.setLevel(logging.WARNING)


def search_client_from_config(acs_config: dict):
    return SearchClient(endpoint=acs_config['endpoint'],
                        index_name=acs_config['index_name'],
                        credential=acs_config['credential'],
                        api_version=acs_config['api_version'])


def create_search_index_sdk(acs_config: dict):
    logger.info(f"Ensuring search index {acs_config['index_name']} exists", extra={'print': True})
    index_client = SearchIndexClient(endpoint=acs_config['endpoint'],
                                    credential=acs_config['credential'])
    if acs_config['index_name'] not in index_client.list_index_names():
        index = SearchIndex(
            name=acs_config['index_name'],
            fields=[
                SimpleField(name="id", type="Edm.String", key=True),
                SearchableField(name="content", type="Edm.String", analyzer_name="en.microsoft"),
                SimpleField(name="category", type="Edm.String", filterable=True, facetable=True),
                SimpleField(name="sourcepage", type="Edm.String", filterable=True, facetable=True),
                SimpleField(name="sourcefile", type="Edm.String", filterable=True, facetable=True),
                SimpleField(name="title", type="Edm.String", filterable=True, facetable=True),
                SimpleField(name="content_hash", type="Edm.String", filterable=True, facetable=True),
                SimpleField(name="meta_json_string", type="Edm.String", filterable=True, facetable=True)
                # TODO: Support constructing typed metadata schema, need to ensure there's consistency across file types, with a section for differing meta that is just string.
                #ComplexField(name="meta", fields=dict_to_fields()),
                # TODO: Insert embeddings once SDK supports it.
                #SearchField(name=f"embedding_vector_{emb.kind}", type="Collection(Edm.Single)", searchable=False), # dimensions=embedding_dimensions), # , retrievable=True
            ],
            semantic_settings=SemanticSettings(
                configurations=[SemanticConfiguration(
                    name='default',
                    prioritized_fields=PrioritizedFields(
                        title_field=None, prioritized_content_fields=[SemanticField(field_name='content')]))])
        )
        logger.info(f"Creating {acs_config['index_name']} search index", extra={'print': True})
        index_client.create_index(index)
    else:
        logger.info(f"Search index {acs_config['index_name']} already exists", extra={'print': True})


@tenacity.retry(
    wait=tenacity.wait_fixed(5),  # wait 5 seconds between retries
    stop=tenacity.stop_after_attempt(3),  # stop after 3 attempts
    reraise=True,  # re-raise the exception after the last retry attempt
)
def send_put_request(url, headers, payload):
    response = requests.put(url, data=json.dumps(payload), headers=headers)

    # Raise an exception if the response contains an HTTP error status code
    response.raise_for_status()
    return response


def create_search_index_rest(acs_config: dict, embeddings: Optional[Embeddings] = None):
    # TODO: Ask users in private preview to provide the new api_version? 2023-07-01-Preview
    logger.info(f"Ensuring search index {acs_config['index_name']} exists", extra={'print': True})
    index_client = SearchIndexClient(endpoint=acs_config['endpoint'],
                                    credential=acs_config['credential'])
    if acs_config['index_name'] not in index_client.list_index_names():
        if 'api_version' not in acs_config:
            acs_config['api_version'] = "2023-07-01-preview"
        base_url = f"{acs_config['endpoint']}/indexes/{acs_config['index_name']}?api-version={acs_config['api_version']}"
        headers = {
            "Content-Type": "application/json"
        }
        if isinstance(acs_config['credential'], DefaultAzureCredential):
            headers["Authorization"] = f"Bearer {acs_config['credential'].get_token('https://search.azure.com/.default').token}"
        else:
            headers["api-key"] = acs_config['credential'].key

        payload = {
            "name": acs_config['index_name'],
            "fields": [
                {"name": "id", "type": "Edm.String", "key": True},
                {"name": "content", "type": "Edm.String", "searchable": True},
                {"name": "category", "type": "Edm.String", "filterable": True, "facetable": True},
                {"name": "sourcepage", "type": "Edm.String", "filterable": True, "facetable": True},
                {"name": "sourcefile", "type": "Edm.String", "filterable": True, "facetable": True},
                {"name": "title", "type": "Edm.String", "filterable": True, "facetable": True},
                {"name": "content_hash", "type": "Edm.String", "filterable": True, "facetable": True},
                {"name": "meta_json_string", "type": "Edm.String", "filterable": True, "facetable": True},
            ],
            "semantic": {
                "configurations": [
                    {
                        "name": "default",
                        "prioritizedFields": {
                            "titleField": {"fieldName": "title"},
                            "prioritizedContentFields": [{"fieldName": "content"}],
                            "prioritizedKeywordsFields": [],
                        },
                    }
                ]
            },
        }

        if embeddings and embeddings.kind != "none":
            field_name = f"content_vector_{embeddings.kind}"
            payload['fields'].append({
                "name": field_name,
                "type": "Collection(Edm.Single)",
                "searchable": True,
                "retrievable": True,
                "dimensions": embeddings.get_embedding_dimensions(),
                "vectorSearchConfiguration": f"{field_name}_config"
            })
            payload['vectorSearch'] = {
                "algorithmConfigurations": [
                    {
                        "name": f"{field_name}_config",
                        "kind": "hnsw",
                        "hnswParameters": {
                            "m": 4,
                            "efConstruction": 400,
                            "metric": "cosine"
                        }
                    }
                ]
            }

        try:
            response = send_put_request(base_url, headers, payload)
            logger.info(response)
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}\nResponse: {e.response.text}")
            raise e
    else:
        logger.info(f"Search index {acs_config['index_name']} already exists", extra={'print': True})


def upsert_documents_sdk():
    pass

def upsert_documents_rest():
    pass


def create_index_from_raw_embeddings(emb: Embeddings, acs_config={}, output_path: Optional[str] = None):
    logger.info("Updating ACS index", extra={'print': True})

    if 'push_embeddings' in acs_config:
        create_search_index_rest(acs_config, emb)
    else:
        create_search_index_sdk(acs_config)

    search_client = search_client_from_config(acs_config)

    batch_size = acs_config['batch_size'] if 'batch_size' in acs_config else 100

    t1 = time.time()
    num_source_docs = 0
    batch = []
    for doc_id, emb_doc in emb._document_embeddings.items():
        logger.info(f'Adding document: {doc_id}', extra={'print': True})
        acs_doc = {
            "id": base64.urlsafe_b64encode(doc_id.encode('utf-8')).decode('utf-8'),
            "content": emb_doc.get_data(),
            "category": "document",
            "sourcepage": emb_doc.metadata.get("source", {}).get("url"),
            "sourcefile": emb_doc.metadata.get("source", {}).get("filename"),
            "title": emb_doc.metadata.get("source", {}).get("title"),
            "content_hash": emb_doc.document_hash,
            "meta_json_string": json.dumps(emb_doc.metadata),
        }

        if 'push_embeddings' in acs_config:
            acs_doc[f"content_vector_{emb.kind}"] = emb_doc.get_embeddings()

        batch.append(acs_doc)
        if len(batch) % batch_size == 0:
            logger.info(f"Sending {len(batch)} documents to ACS", extra={'print': True})
            start_time = time.time()
            results = search_client.upload_documents(documents=batch)
            succeeded = []
            failed = []
            for r in results:
                if r.succeeded:
                    succeeded.append(r)
                else:
                    failed.append(r)
            logger.info(f"Uploaded {len(succeeded)} documents to ACS in {time.time() - start_time:.4f} seconds, {len(failed)} failed", extra={'print': True})
            if len(failed) > 0:
                logger.error(f"Failed documents: {failed}", extra={'print': True})
            batch = []
            num_source_docs += batch_size

    if len(batch) > 0:
        logger.info(f"Sending {len(batch)} documents to ACS", extra={'print': True})
        start_time = time.time()
        results = search_client.upload_documents(documents=batch)
        succeeded = sum(1 for r in results if r.succeeded)
        logger.info(f"Uploaded {succeeded} documents to ACS in {time.time() - start_time:.4f} seconds, {len(batch) - succeeded} failed", extra={'print': True})

        num_source_docs += len(batch)

    logger.info(f"Built index from {num_source_docs} documents and {len(emb._document_embeddings)} chunks, took {time.time()-t1:.4f} seconds", extra={'print': True})

    if output_path is not None:
        logger.info('Writing MLIndex yaml', extra={'print': True})
        mlindex_config = {
            "embeddings": emb.get_metadata()
        }
        mlindex_config["index"] = {
            "kind": "acs",
            "engine": "azure-sdk",
            "index": acs_config['index_name'],
            "api_version": acs_config['api_version'],
            "field_mapping": {
                "content": "content",
                "url": "sourcepage",
                "filename": "sourcefile",
                "title": "title",
                "metadata": "meta_json_string",
            }
        }
        if 'push_embeddings' in acs_config:
            mlindex_config["index"]["field_mapping"]["embedding"] = f"content_vector_{emb.kind}"

        if isinstance(acs_config['credential'], AzureKeyCredential):
            from azureml.core import Run
            run = Run.get_context()
            ws = run.experiment.workspace
            mlindex_config["index"]["connection_type"] = "workspace_keyvault"
            mlindex_config["index"]["connection"] = {
                "subscription": ws.subscription_id,
                "resource_group": ws.resource_group,
                "workspace": ws.name,
                "key": acs_config['endpoint_key_name']
            }
        # Keyvault auth and Default ambient auth need the endpoint, Workspace Connection auth could get endpoint.
        mlindex_config["index"]["endpoint"] = acs_config['endpoint']
        output = Path(output_path)
        output.mkdir(parents=True, exist_ok=True)
        with open(output / "MLIndex", "w") as f:
            yaml.dump(mlindex_config, f)


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("--embeddings", type=str)
    parser.add_argument("--acs_config", type=str)
    parser.add_argument("--output", type=str)
    args = parser.parse_args()

    print('\n'.join(f'{k}={v}' for k, v in vars(args).items()))

    enable_stdout_logging()

    raw_embeddings_uri = args.embeddings
    logger.info(f'got embeddings uri as input: {raw_embeddings_uri}', extra={'print': True})
    splits = raw_embeddings_uri.split('/')
    embeddings_dir_name = splits.pop(len(splits)-2)
    logger.info(f'extracted embeddings directory name: {embeddings_dir_name}', extra={'print': True})
    parent = '/'.join(splits)
    logger.info(f'extracted embeddings container path: {parent}', extra={'print': True})

    acs_config = json.loads(args.acs_config)

    if 'endpoint_key_name' in acs_config:
        from azure.core.credentials import AzureKeyCredential
        name = acs_config['endpoint_key_name']
        key = get_secret_from_workspace(name)
        acs_config['credential'] = AzureKeyCredential(key)
    else:
        from azure.identity import DefaultAzureCredential
        acs_config['credential'] = DefaultAzureCredential()

    from azureml.dataprep.fuse.dprepfuse import (MountOptions, rslex_uri_volume_mount)
    mnt_options = MountOptions(
        default_permission=0o555, allow_other=False, read_only=True)
    logger.info(f'mounting embeddings container from: \n{parent} \n   to: \n{os.getcwd()}/embeddings_mount', extra={'print': True})
    with rslex_uri_volume_mount(parent, f'{os.getcwd()}/embeddings_mount', options=mnt_options) as mount_context:
        emb = Embeddings.load(embeddings_dir_name, mount_context.mount_point)
        create_index_from_raw_embeddings(emb, acs_config=acs_config, output_path=args.output)

    logger.info('Updated ACS index', extra={'print': True})
