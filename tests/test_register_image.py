#! /usr/bin/env python

"""
Tests for the clonebuildregister module.
"""

import unittest

import docker

from testing_variables import GCLOUD_PROJECT, GCLOUD_REPOSITORY, GCLOUD_LOCATION


from clonebuildregister import register_image
from clonebuildregister import build_image


class TestRegisterImage(unittest.TestCase):
    """Test registerImage in the bimage module. Relies on buildImage"""

    def setUp(self):
        """Tests set up"""

        build_image.build_image("testimage:v2", "tests")

    def test_register_image(self):
        """Test register_image.register_image."""
        response = register_image.register_image(
            "testimage",
            "v2",
            "test-image-out",
            "v1",
            f"{GCLOUD_LOCATION}",
            f"{GCLOUD_PROJECT}",
            f"{GCLOUD_REPOSITORY}",
        )
        self.assertFalse("errorDetail" in response)
        client = docker.from_env()
        client.images.remove("continuumio/miniconda3:latest")

        client.images.remove("testimage:v2")
        client.images.remove(
            f"{GCLOUD_LOCATION}-docker.pkg.dev/{GCLOUD_PROJECT}/{GCLOUD_REPOSITORY}/test-image-out:v1"
        )

    def test_register_image_delete_all_image_param(self):
        """Test register_image.register_image."""
        response = register_image.register_image(
            "testimage",
            "v2",
            "test-image-out",
            "v1",
            f"{GCLOUD_LOCATION}",
            f"{GCLOUD_PROJECT}",
            f"{GCLOUD_REPOSITORY}",
            delete_all_docker_images=True,
        )
        self.assertFalse("errorDetail" in response)
        client = docker.from_env()

        self.assertEqual(0, len(client.images.list()))
