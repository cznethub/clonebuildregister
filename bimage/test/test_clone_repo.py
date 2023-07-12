#! /usr/bin/env python

"""
Tests for the bimage module.
"""

import os
import shutil
import unittest

from bimage import clone_repo


class TestCloneRepo(unittest.TestCase):
    """Test functions in the bimage module."""

    def tearDown(self):
        """Test fixture destroy."""
        shutil.rmtree("timage")

    def test_clonerepo(self):
        """Test bimage.bimage."""
        clone_repo.clone_repo("cbcunc", "timage", "develop")
        self.assertTrue(os.path.exists("timage"))
