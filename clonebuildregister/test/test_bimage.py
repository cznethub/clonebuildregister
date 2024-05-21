#! /usr/bin/env python

"""
Tests for the clonebuildregister module.
"""
# Standard lib
import os
import unittest
import shutil

import docker

from clonebuildregister import clonebuildregister
from .testing_variables import GCLOUD_PROJECT, GCLOUD_REPOSITORY, \
GCLOUD_LOCATION, GITHUB_REPO_ORG, GITHUB_REPO_NAME, GITHUB_REPO_BRANCH


class TestBuildImage(unittest.TestCase):
    """Test functions in the clonebuildregister module."""

    def tearDown(self):
        """Test fixture destroy."""

        client = docker.from_env()
        client.images.remove("continuumio/miniconda3:latest")
        client.images.remove("testimage:v1")

        shutil.rmtree(GITHUB_REPO_NAME)

        client.images.remove(
            f"{GCLOUD_LOCATION}-docker.pkg.dev/{GCLOUD_PROJECT}/{GCLOUD_REPOSITORY}/testimage:v1"
        )

    def test_clonebuildregister(self):
        """Test clonebuildregister.clonebuildregister."""

        response = clonebuildregister.clonebuildregister(GITHUB_REPO_ORG, GITHUB_REPO_NAME, GITHUB_REPO_BRANCH, "testimage", "v1", "timage",
                          "testimage", "v1", f"{GCLOUD_LOCATION}", f"{GCLOUD_PROJECT}", f"{GCLOUD_REPOSITORY}"
                          )
        client = docker.from_env()
        self.assertTrue(len(client.images.list(name="testimage")) > 0)

        self.assertTrue(os.path.exists(GITHUB_REPO_NAME))

        self.assertFalse("errorDetail" in response)
