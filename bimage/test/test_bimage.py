#! /usr/bin/env python

"""
Tests for the bimage module.
"""
# Standard lib
import os
import unittest
import shutil

import docker

from bimage import bimage


class TestBuildImage(unittest.TestCase):
    """Test functions in the bimage module."""

    def tearDown(self):
        """Test fixture destroy."""

        client = docker.from_env()
        client.images.remove("continuumio/miniconda3:latest")
        client.images.remove("testimage:v1")

        shutil.rmtree("timage")

        client.images.remove(
            "us-east1-docker.pkg.dev/bimage-project-423316/bimage-repository/testimage:v1"
        )

    def test_bimage(self):
        """Test bimage.bimage."""

        response = bimage.bimage("cbcunc", "timage", "develop", "testimage", "v1", "timage",
                          "testimage", "v1", "us-east1", "bimage-project-423316", "bimage-repository"
                          )
        client = docker.from_env()
        self.assertTrue(len(client.images.list(name="testimage")) > 0)

        self.assertTrue(os.path.exists("timage"))

        self.assertFalse("errorDetail" in response)
