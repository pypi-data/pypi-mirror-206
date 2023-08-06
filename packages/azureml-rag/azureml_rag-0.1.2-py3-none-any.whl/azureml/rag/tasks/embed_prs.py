# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import argparse
import os
import pandas as pd
import pathlib
import time

from azureml.rag.embeddings import Embeddings
from azureml.rag.tasks.embed import read_chunks_into_documents
from azureml.rag.utils.logging import get_logger, enable_stdout_logging


logger = get_logger('embed')


def init():
    global output_data
    global previous_embeddings
    parser = argparse.ArgumentParser(allow_abbrev=False, description="ParallelRunStep Agent")
    parser.add_argument("--output_data", type=str)
    parser.add_argument("--embeddings_model", type=str)
    parser.add_argument("--previous_embeddings", required=False, type=str, default=None)
    args, _ = parser.parse_known_args()

    print('\n'.join(f'{k}={v}' for k, v in vars(args).items()))

    enable_stdout_logging()

    output_data = args.output_data

    previous_embeddings = None
    if args.previous_embeddings is not None:
        from azureml.dataprep.fuse.dprepfuse import MountOptions, rslex_uri_volume_mount
        mnt_options = MountOptions(
            default_permission=0o555, allow_other=False, read_only=True)
        try:
            with rslex_uri_volume_mount(args.previous_embeddings, f'{os.getcwd()}/previous_embeddings', options=mnt_options) as mount_context:
                previous_embeddings_dir_name = None
                # list all folders in previous_embeddings_container_path and find the latest one
                try:
                    previous_embeddings_dir_name = str(max([dir for dir in pathlib.Path(
                        mount_context.mount_point).glob('*') if dir.is_dir() and dir.name != os.environ['AZUREML_RUN_ID']], key=os.path.getmtime).name)
                except Exception as e:
                    logger.warn(
                        f'failed to get latest folder from {mount_context.mount_point} with {e}.', extra={'print': True})
                    pass

                if previous_embeddings_dir_name is not None:
                    logger.info(
                        f'loading from previous embeddings from {previous_embeddings_dir_name} in {mount_context.mount_point}', extra={'print': True})
                    try:
                        previous_embeddings = Embeddings.load(
                            previous_embeddings_dir_name, mount_context.mount_point)
                    except Exception as e:
                        logger.warn(
                            f'Failed to load from previous embeddings with {e}.\nCreating new Embeddings.', extra={'print': True})
        except Exception as e:
            logger.warn(f'Failed to load previous embeddings from mount with {e}, proceeding to create new embeddings.', extra={'print': True})

    previous_embeddings = previous_embeddings if previous_embeddings is not None else Embeddings.from_uri(args.embeddings_model)


# TODO: Not handling throttling from openai api, need to back off more
def _run_internal(mini_batch, output_data, embeddings):
    """
    Internal run method, primarily used for unit tests.

    :param mini_batch: The list of files to be processed.
    :param output_data: The output folder to save data to.
    :param embeddings: The Embeddings object that should be used to embed new data.
    """
    logger.info(f'run method start: {__file__}, run({mini_batch})', extra={'print': True})
    logger.info(f'Task id: {mini_batch.task_id}', extra={'print': True})

    # read chunks
    pre_embed = time.time()
    embeddings = embeddings.embed_and_create_new_instance(read_chunks_into_documents((pathlib.Path(p) for p in mini_batch)))
    post_embed = time.time()
    logger.info(f"Embedding took {post_embed - pre_embed} seconds", extra={'print': True})

    save_metadata = str(mini_batch.task_id) == '0'
    if save_metadata:
        logger.info('Metadata will be saved', extra={'print': True})
    else:
        logger.info('Only data will be saved', extra={'print': True})
    embeddings.save(output_data, with_metadata=save_metadata, suffix=mini_batch.task_id)


def run(mini_batch):
    _run_internal(mini_batch, output_data, previous_embeddings)
    return pd.DataFrame({"Files": [os.path.split(file)[-1] for file in mini_batch]})
