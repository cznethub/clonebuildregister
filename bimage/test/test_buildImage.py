#! /usr/bin/env python

"""
Tests for the bimage module.
"""


import unittest
import sys
import docker
sys.path.append('..')
from bimage import buildImage
import os
import shutil


class TestBuildImage(unittest.TestCase):
    """Test functions in the bimage module."""

    def setUp(self):
        """Opens a DockerFile and a simple html file to build."""
        
        # os.chdir("bimage/test")
        
        #f = open("index.html", 'a')
        #f.write("<h1/>This is an h1 tag<h1>")
        #.close()

    def tearDown(self):
        """Test fixture destroy."""
        
        #os.remove("index.html")
        client = docker.from_env()

        client.images.remove("continuumio/miniconda3:latest")
        client.images.remove("testimage:v1")
        # client.images.remove(image[0].short_id)
        # client.images.remove("continuumio/miniconda3")
        
        

    def test_bimage(self):
        """Test bimage.bimage."""

        image = buildImage.buildImage("testimage:v1", "")
        
        client = docker.from_env()

        self.assertTrue(len(client.images.list(name="testimage")) > 0)
        
