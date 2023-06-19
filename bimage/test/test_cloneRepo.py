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

    def setUp(self):
        """Test fixture build."""
        
        cloneRepo.cloneRepo("cbcunc", "timage", "develop")

    def tearDown(self):
        """Test fixture destroy."""
        
        shutil.rmtree("timage")

    def test_clonerepo(self):
        """Test bimage.bimage."""
        
        self.assertTrue(os.path.exists("timage"))