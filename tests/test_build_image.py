#! /usr/bin/env python

"""
Tests for the clonebuildregister module.
"""

import unittest

import docker

from clonebuildregister.build_image import build_image


class TestBuildImage(unittest.TestCase):
    """Test functions in the clonebuildregister module."""

    def tearDown(self):
        """Test fixture destroy."""
        client = docker.from_env()

        print("Attempting to delete remaining local images. Deleting using --force.")
        for image in client.images.list():
            print("Deleting image: ", image.tags)
            client.images.remove(image.id, force=True)

    def test_build_image(self):
        """Test clonebuildregister.clonebuildregister."""
        build_image("testimage:v1", "tests")

        client = docker.from_env()

        self.assertTrue(len(client.images.list(name="testimage")) > 0)

    def test_build_image_with_platform(self):
        """Test clonebuildregister.clonebuildregister. with a platform field"""
        build_image("testimage:v1", "tests", platform="linux/amd64")

        client = docker.from_env()

        self.assertTrue(len(client.images.list(name="testimage")) > 0)

    def test_build_image_copy_env(self):
        """Test clone repo with arguments defining environment variables,
        essentially all it does it tests the copying of environment files"""
        build_image(
            "testimage:v1",
            "tests",
            "tests/buildImageTest.env",
            "tests/buildImageTestFolder/buildImageTest.env",
        )
        with open(
            "tests/buildImageTestFolder/buildImageTest.env", "r", encoding="UTF-8"
        ) as file_desc:
            read_bytes = file_desc.read()
            self.assertEqual("CAT=MEOW", read_bytes)

        # rewriting the image as it was before
        with open(
            "tests/buildImageTestFolder/buildImageTest.env", "w", encoding="UTF-8"
        ) as file_desc:
            file_desc.write("DOG=RUFF")
            file_desc.close()
        client = docker.from_env()
        self.assertTrue(len(client.images.list(name="testimage")) > 0)

    def test_build_image_load_env(self):
        """Test clone repo with arguments defining environment variables, \
            testing whether env variables are imported for image"""
        build_image(
            "testimage:v1", "tests/testArgDockerfile", "tests/buildImageTest.env"
        )

        client = docker.from_env()
        output = client.containers.run("testimage:v1")
        self.assertEqual(b"The cat goes, MEOW\n", output)
        self.assertTrue(len(client.images.list(name="testimage")) > 0)
