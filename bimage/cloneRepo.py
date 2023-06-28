#! /usr/bin/env python

"""
The cloneRepo module.
"""

import github3
import git
import shutil

def cloneRepo(github_org: str, repo_name: str, branch_or_tag: str, path_to_local_environment: str="", path_to_remote_environment: str=""):
    """Clones a repository from github, and can optionally overwrite env files in the repository with something local

    Args:
        github_org (str)                            The GitHub organization of the repository
        repo_name (str)                             The name of the repository in the organization
        branch_or_tag (str)                         The branch or tag of the repository
        path_to_local_environment (str, optional):  The path to a local environment file with secrets not to be seen on github (e.g usr/home/bimage/.env).. Defaults to "".
        path_to_remote_environment (str, optional): The path to the dummy environment files found on github (e.g usr/home/bimage/.env). Defaults to "".
    """
    if (path_to_local_environment != "" and path_to_remote_environment != ""):
        shutil.copyfile(path_to_local_environment, path_to_remote_environment)
        
    gh = github3.GitHub()
    repo = gh.repository(github_org, repo_name)
    clone = git.Repo.clone_from(repo.clone_url, repo_name)
    clone.git.checkout(branch_or_tag)
    return