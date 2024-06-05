#! /usr/bin/env python

"""
Tests for the clonebuildregister module.
"""
# Standard lib
import os
import unittest
import shutil

import docker
from testing_variables import (
    GCLOUD_PROJECT,
    GCLOUD_REPOSITORY,
    GCLOUD_LOCATION,
    GITHUB_REPO_ORG,
    GITHUB_REPO_NAME,
    GITHUB_REPO_BRANCH,
)

from clonebuildregister import clonebuildregister


class TestBuildImage(unittest.TestCase):
    """Test functions in the clonebuildregister module."""

    def tearDown(self):
        """Test fixture destroy."""

        client = docker.from_env()
        print("Attempting to delete remaining local images. Deleting using --force.")
        for image in client.images.list():
            print("Deleting image: ", image.tags)
            client.images.remove(image.id, force=True)

    def test_clonebuildregister(self):
        """Test clonebuildregister.clonebuildregister."""

        response = clonebuildregister.clonebuildregister(
            GITHUB_REPO_ORG,
            GITHUB_REPO_NAME,
            GITHUB_REPO_BRANCH,
            "testimage",
            "v1",
            "timage",
            "testimage",
            "v1",
            f"{GCLOUD_LOCATION}",
            f"{GCLOUD_PROJECT}",
            f"{GCLOUD_REPOSITORY}",
        )
        client = docker.from_env()
        self.assertTrue(len(client.images.list(name="testimage")) > 0)

        self.assertTrue(os.path.exists(GITHUB_REPO_NAME))

        self.assertFalse("errorDetail" in response)

        shutil.rmtree(GITHUB_REPO_NAME)

    def test_clonebuildregister_delete_repository(self):
        """Test clonebuildregister.clonebuildregister."""

        response = clonebuildregister.clonebuildregister(
            GITHUB_REPO_ORG,
            GITHUB_REPO_NAME,
            GITHUB_REPO_BRANCH,
            "testimage",
            "v1",
            GITHUB_REPO_NAME,
            "testimage",
            "v1",
            f"{GCLOUD_LOCATION}",
            f"{GCLOUD_PROJECT}",
            f"{GCLOUD_REPOSITORY}",
            delete_repository=True,
        )
        client = docker.from_env()
        self.assertTrue(len(client.images.list(name="testimage")) > 0)

        self.assertFalse(
            os.path.exists(GITHUB_REPO_NAME)
        )  # we need to make sure that repository is deleted after program finishes

        self.assertFalse("errorDetail" in response)

    def test_clonebuildregister_delete_repository_with_clone_name(self):
        """Test clonebuildregister.clonebuildregister."""

        test_repo_name = "abritraryname"

        response = clonebuildregister.clonebuildregister(
            GITHUB_REPO_ORG,
            GITHUB_REPO_NAME,
            GITHUB_REPO_BRANCH,
            "testimage",
            "v1",
            test_repo_name,
            "testimage",
            "v1",
            f"{GCLOUD_LOCATION}",
            f"{GCLOUD_PROJECT}",
            f"{GCLOUD_REPOSITORY}",
            delete_repository=True,
            clone_name=test_repo_name,
        )
        client = docker.from_env()
        self.assertTrue(len(client.images.list(name="testimage")) > 0)

        self.assertFalse(
            os.path.exists(test_repo_name)
        )  # we need to make sure that repository is deleted after program finishes

        self.assertFalse("errorDetail" in response)
