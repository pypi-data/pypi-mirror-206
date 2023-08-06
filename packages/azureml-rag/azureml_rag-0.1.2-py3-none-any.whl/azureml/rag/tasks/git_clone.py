# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import argparse

from azureml.rag.utils.git import clone_repo
from azureml.rag.utils.logging import get_logger, enable_stdout_logging

logger = get_logger('git_clone')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--git-repository", type=str, required=True, dest='git_repository')
    parser.add_argument("--branch-name", type=str, required=False, default=None)
    parser.add_argument("--authentication-key-prefix", type=str, required=False, default=None, help="<PREFIX>-USER and <PREFIX>-PASS are the expected names of two Secrets in the Workspace Key Vault which will be used for authenticated when pulling the given git repo.")
    parser.add_argument("--output-data", type=str, required=True, dest='output_data')
    args = parser.parse_args()

    enable_stdout_logging()

    clone_repo(args.git_repository, args.output_data, args.branch_name, args.authentication_key_prefix)

    logger.info('Finished cloning.')
