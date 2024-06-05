#! /usr/bin/env python

"""
Tests for the bimage module.
"""

import os
import shutil
import unittest

from testing_variables import GITHUB_REPO_ORG, GITHUB_REPO_NAME, GITHUB_REPO_BRANCH

from clonebuildregister import clone_repo


class TestCloneRepo(unittest.TestCase):
    """Test functions in the clone_repo module."""

    def test_clonerepo(self):
        """Test clonebuildregister.clone_repo."""
        clone_repo.clone_repo(GITHUB_REPO_ORG, GITHUB_REPO_NAME, GITHUB_REPO_BRANCH)
        self.assertTrue(os.path.exists(GITHUB_REPO_NAME))
        shutil.rmtree(GITHUB_REPO_NAME)

    def test_clonerepo_with_clonename_parameter(self):
        """Test clonebuildregister.clone_repo."""
        test_repo_name = "abritraryname"
        clone_repo.clone_repo(
            GITHUB_REPO_ORG,
            GITHUB_REPO_NAME,
            GITHUB_REPO_BRANCH,
            clone_name=test_repo_name,
        )
        self.assertTrue(os.path.exists(test_repo_name))
        shutil.rmtree(test_repo_name)
