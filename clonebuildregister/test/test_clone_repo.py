#! /usr/bin/env python

"""
Tests for the bimage module.
"""

import os
import shutil
import unittest

from clonebuildregister import clone_repo
from .testing_variables import GITHUB_REPO_ORG, GITHUB_REPO_NAME, GITHUB_REPO_BRANCH

class TestCloneRepo(unittest.TestCase):
    """Test functions in the clone_repo module."""

    def tearDown(self):
        """Test fixture destroy."""
        shutil.rmtree(GITHUB_REPO_NAME)

    def test_clonerepo(self):
        """Test clonebuildregister.clone_repo."""
        clone_repo.clone_repo(GITHUB_REPO_ORG, GITHUB_REPO_NAME, GITHUB_REPO_BRANCH)
        self.assertTrue(os.path.exists(GITHUB_REPO_NAME))
