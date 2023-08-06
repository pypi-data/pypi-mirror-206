# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import numpy as np
import os
from pathlib import Path
import time
import yaml

from langchain.docstore.document import Document
from langchain.docstore.in_memory import InMemoryDocstore
from langchain.vectorstores import FAISS
from langchain.vectorstores.faiss import dependable_faiss_import

from azureml.rag.embeddings import Embeddings
from azureml.rag.utils.logging import get_logger, enable_stdout_logging


logger = get_logger('build_faiss')


def create_index_from_raw_embeddings(embeddings_container: str, embeddings_directory: str, output_path):
    logger.info("Loading Embeddings", extra={'print': True})
    emb = Embeddings.load(embeddings_directory, embeddings_container)

    logger.info("Building index", extra={'print': True})
    t1 = time.time()
    num_source_docs = 0
    documents = []
    embeddings = []
    for doc_id, emb_doc in emb._document_embeddings.items():
        logger.info(f'Adding document: {doc_id}', extra={'print': True})
        logger.debug(f'{doc_id},{emb_doc.document_hash},{emb_doc.get_embeddings()[0:20]}', extra={'print': True})
        embeddings.append(emb_doc.get_embeddings())
        # TODO: LazyDocument/RefDocument gets uri to page_content
        documents.append(Document(page_content=emb_doc.get_data(),
                                    metadata={"source_doc_id": doc_id,
                                            "chunk_hash": emb_doc.document_hash,
                                            "mtime": emb_doc.mtime,
                                            **emb_doc.metadata}))
        num_source_docs += 1

    index_to_id = {i: doc.metadata["source_doc_id"] for i, doc in enumerate(documents)}
    docstore = InMemoryDocstore(
        {index_to_id[i]: doc for i, doc in enumerate(documents)}
    )

    faiss = dependable_faiss_import()
    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(np.array(embeddings, dtype=np.float32))

    faiss_index = FAISS(emb.get_query_embed_fn(), index, docstore, index_to_id)

    logger.info(f"Built index from {num_source_docs} documents and {len(embeddings)} chunks, took {time.time()-t1:.4f} seconds", extra={'print': True})

    logger.info("Saving index", extra={'print': True})
    faiss_index.save_local(output_path)

    mlindex_config = {
        "embeddings": emb.get_metadata()
    }
    mlindex_config["index"] = {
        "kind": "faiss",
        "method": "FlatL2",
        "engine": "langchain.vectorstores.FAISS",
    }
    with open(Path(output_path) / "MLIndex", "w") as f:
        yaml.dump(mlindex_config, f)


def register_run_output(output_data, asset_name):
    from azureml.core.run import Run
    from azureml.core import Dataset
    from azureml.data.datapath import DataPath

    current_run = Run.get_context()
    if hasattr(current_run, 'experiment'):
        ws = current_run.experiment.workspace
        datastore = ws.get_default_datastore()
        embeddings_ds = Dataset.File.upload_directory(src_dir=output_data,
           target=DataPath(datastore,  asset_name),
           show_progress=True)
        embeddings_ds.register(workspace=ws,
                               name=asset_name,
                               description=f"Embeddings for dataset_name: {asset_name}",
                               create_new_version=True)


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("--embeddings", type=str)
    parser.add_argument("--output", type=str)
    parser.add_argument("--asset_name", type=str)
    parser.add_argument("--register_output", type=str)
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

    # Mock OPENAI_API_KEY being set so that loading Embeddings doesn't fail, we don't need to do any embedding so should be fine
    os.environ['OPENAI_API_KEY'] = 'nope'

    from azureml.dataprep.fuse.dprepfuse import (MountOptions, rslex_uri_volume_mount)
    mnt_options = MountOptions(
        default_permission=0o555, allow_other=False, read_only=True)
    logger.info(f'mounting embeddings container from: \n{parent} \n   to: \n{os.getcwd()}/raw_embeddings', extra={'print': True})
    with rslex_uri_volume_mount(parent, f'{os.getcwd()}/raw_embeddings', options=mnt_options) as mount_context:
        create_index_from_raw_embeddings(mount_context.mount_point, embeddings_dir_name, args.output)

    logger.info('Generated FAISS index', extra={'print': True})

    # TODO: Replace with output data def that registers new version
    register_output = args.register_output == "True" or args.register_output == "true"
    if register_output:
        register_run_output(args.output, args.asset_name)
