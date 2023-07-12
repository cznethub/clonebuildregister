#! /usr/bin/env python

"""
Tests for the bimage module.
"""

import unittest

import docker

from ..bimage import build_image


class TestBuildImage(unittest.TestCase):
    """Test functions in the bimage module."""

    def tearDown(self):
        """Test fixture destroy."""

        client = docker.from_env()

        client.images.remove("testimage:v1", force=True)
        client.images.remove("continuumio/miniconda3:latest", force=True)


    def test_build_image(self):
        """Test bimage.bimage."""
        build_image("testimage:v1", "bimage/test")

        client = docker.from_env()

        self.assertTrue(len(client.images.list(name="testimage")) > 0)

    def test_build_image_copy_env(self):
        """Test clone repo with arguments defining environment variables,
            essentially all it does it tests the copying of environment files"""
        build_image(
                    "testimage:v1", "bimage/test", "bimage/test/buildImageTest.env",
                    "bimage/test/buildImageTestFolder/buildImageTest.env"
                    )
        with open("bimage/test/buildImageTestFolder/buildImageTest.env", "r", encoding='UTF-8') as file_desc:
            read_bytes = file_desc.read()
            self.assertEqual("CAT=MEOW", read_bytes)

        # rewriting the image as it was before
        with open("bimage/test/buildImageTestFolder/buildImageTest.env", "w", encoding='UTF-8') as file_desc:
            file_desc.write("DOG=RUFF")
            file_desc.close()
        client = docker.from_env()
        self.assertTrue(len(client.images.list(name="testimage")) > 0)

    def test_build_image_load_env(self):
        """Test clone repo with arguments defining environment variables, \
            testing whether env variables are imported for image"""
        build_image(
            "testimage:v1", "bimage/test/testArgDockerfile", "bimage/test/buildImageTest.env"
        )

        client = docker.from_env()
        output = client.containers.run('testimage:v1')
        self.assertEqual(b"The cat goes, MEOW\n", output)
        self.assertTrue(len(client.images.list(name="testimage")) > 0)
