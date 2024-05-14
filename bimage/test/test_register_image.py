#! /usr/bin/env python

"""
Tests for the bimage module.
"""

import unittest

import docker

from bimage import register_image
from bimage import build_image



class TestRegisterImage(unittest.TestCase):
    """Test registerImage in the bimage module. Relies on buildImage"""
    def setUp(self):
        """ Tests set up """
        
        build_image.build_image("testimage:v2", "bimage/test")

    def tearDown(self):
        """Test fixture destroy."""

        client = docker.from_env()
        client.images.remove("continuumio/miniconda3:latest")

        client.images.remove("testimage:v2")
        client.images.remove(
            "us-east1-docker.pkg.dev/bimage-project-423316/bimage-repository/test-image-out:v1"
        )

    def test_register_image(self):
        """Test bimage.bimage."""
        response = register_image.register_image(
            "testimage", "v2", "test-image-out", "v1", "us-east1", "bimage-project-423316",
            "bimage-repository"
        )
        self.assertFalse("errorDetail" in response)
