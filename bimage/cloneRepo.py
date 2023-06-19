#! /usr/bin/env python

"""
The bimage module.
"""

import github3
import git


def cloneRepo(github_org: str, repo_name: str, branch_or_tag: str):
        """
        The bimage function.

        Parameters:
            github_org     The GitHub organization of the repository
            repo_name      The name of the repository in the organization
            branch_or_tag  The branch or tag of the repository

        Returns: None
        """

        gh = github3.GitHub()
        repo = gh.repository(github_org, repo_name)
        clone = git.Repo.clone_from(repo.clone_url, repo_name)
        clone.git.checkout(branch_or_tag)
        return