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
        cloneRepo.cloneRepo("cbcunc", "timage", "develop")
        self.assertTrue(os.path.exists("timage"))

    def test_cloneRepoEnv(self):
        """Test clone repo with arguments defining environment variables, essentially all it does it tests the copying of environment files"""
        cloneRepo.cloneRepo("cbcunc", "timage", "develop", "cloneRepoTestEnv.env", "cloneRepoTestFolder/cloneRepoTestEnv.env")
        fd = open("cloneRepoTestFolder/cloneRepoTestEnv.env", "r")
        readB = fd.read()
        self.assertEqual("CAT=MEOW", readB)

        # rewriting the image as it was before
        fd.close()

        fd = open("cloneRepoTestFolder/cloneRepoTestEnv.env", "w")
        fd.write("DOG=RUFF")
        fd.close()
