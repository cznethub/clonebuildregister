#! /usr/bin/env python

"""
The cloneRepo module.
"""

import github3
import git

from .exceptions import CloneRepositoryException


def clone_repo(
    github_org: str, repo_name: str, branch_or_tag: str, clone_name: str = ""
):
    """Clones a repository from github, and can optionally overwrite env files in the \
        repository with something local

    Args:
        github_org (str):    The GitHub organization of the repository
        repo_name (str):     The name of the repository in the organization
        branch_or_tag (str): The branch or tag of the repository
        clone_name (str):    Name of the top level directory that github will create locally. \
            Optional,

    """

    git_client = github3.GitHub()
    if clone_name:
        try:
            repo = git_client.repository(github_org, repo_name)
            clone = git.Repo.clone_from(repo.clone_url, clone_name)
            clone.git.checkout(branch_or_tag)
        except Exception as exc:
            raise CloneRepositoryException() from exc
    else:
        try:
            repo = git_client.repository(github_org, repo_name)
            clone = git.Repo.clone_from(repo.clone_url, repo_name)
            clone.git.checkout(branch_or_tag)
        except Exception as exc:
            raise CloneRepositoryException() from exc
