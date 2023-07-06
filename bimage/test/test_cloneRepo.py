#! /usr/bin/env python

"""
Tests for the bimage module.
"""


import unittest
import sys
sys.path.append('..')
from bimage import cloneRepo
import os
import shutil


class TestCloneRepo(unittest.TestCase):
    """Test functions in the bimage module."""
    

    def tearDown(self):
        """Test fixture destroy."""
        shutil.rmtree("timage")

    def test_clonerepo(self):
        """Test bimage.bimage."""
        cloneRepo.clone_repo("cbcunc", "timage", "develop")
        self.assertTrue(os.path.exists("timage"))
