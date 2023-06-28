#! /usr/bin/env python

"""
Tests for the bimage module.
"""


import unittest
import sys
sys.path.append('..')
from bimage import registerImage
from bimage import buildImage
import os
import shutil
import docker


class TestRegisterImage(unittest.TestCase):
    """Test registerImage in the bimage module. Relies on buildImage"""
    def setUp(self):
        """ Tests set up """
        #os.chdir("bimage/test")
        #print(os.getcwd())
        
        buildImage.buildImage("testimage:v2", "")
    def tearDown(self):
        """Test fixture destroy."""
        
        client = docker.from_env()
        client.images.remove("continuumio/miniconda3:latest")

        client.images.remove("testimage:v2")
        client.images.remove("us-east1-docker.pkg.dev/bimage-project/bimage-repository/test-image-out:v1")

    def test_clonerepo(self):
        """Test bimage.bimage."""
        response = registerImage.registerImage("testimage", "v2", "test-image-out", "v1", "us-east1", "bimage-project", "bimage-repository")
        self.assertFalse("errorDetail" in response)