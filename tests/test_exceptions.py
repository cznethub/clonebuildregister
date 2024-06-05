#! /usr/bin/env python

"""
Tests for the bimage module.
"""
import os
import unittest
import docker

from testing_variables import (
    GCLOUD_REPOSITORY,
    GITHUB_REPO_ORG,
    GITHUB_REPO_NAME,
    GITHUB_REPO_BRANCH,
)

from clonebuildregister.clone_repo import clone_repo
from clonebuildregister.build_image import build_image
from clonebuildregister.register_image import register_image
from clonebuildregister.clonebuildregister import clonebuildregister
from clonebuildregister.exceptions import CloneRepositoryException
from clonebuildregister.exceptions import BuildImageException
from clonebuildregister.exceptions import TagImageException
from clonebuildregister.exceptions import BadCopyEnvException
from clonebuildregister.exceptions import GCloudRegisterImageException
from clonebuildregister.exceptions import CBRException


class TestExceptions(unittest.TestCase):
    """Test registerImage in the bimage module. Relies on buildImage"""

    def test_clone_repo_fail(self):
        """This test tries throwing exception on clone_repo"""
        self.assertRaises(
            CloneRepositoryException,
            clone_repo,
            "meow",
            "this_repo_don'texists",
            "1232132tttt",
        )

    def test_clone_repo_fail_with_clonename(self):
        """This test tries throwing exception on clone_repo"""
        self.assertRaises(
            CloneRepositoryException,
            clone_repo,
            "meow",
            "this_repo_don'texists",
            "1232132tttt",
            "oopsies",
        )

    def test_build_image_fail(self):
        """This test tries throwing exception on build_image"""
        self.assertRaises(BuildImageException, build_image, "meow", "/asdfasdf/adsf")

    def test_register_image_fail(self):
        """Test tries building a faulty image"""
        self.assertRaises(
            TagImageException,
            register_image,
            "ruff12",
            "v12",
            "rufff12",
            "v12",
            "idkwhere",
            "this_is_notaproject",
            "funnynamehere",
        )

    def test_push_image_to_gcloud_fail(self):
        """Test tries sending image to gcloud with faulty remote location"""
        build_image("testimage:v1", "tests")

        client = docker.from_env()

        self.assertTrue(len(client.images.list(name="testimage")) > 0)
        self.assertRaises(
            GCloudRegisterImageException,
            register_image,
            "testimage",
            "v1",
            "testimage",
            "v1",
            "notaregion",
            "sillyprojectid",
            "notarepository",
        )

        client.images.remove("testimage:v1", force=True)
        client.images.remove("continuumio/miniconda3:latest", force=True)
        client.images.remove(
            "notaregion-docker.pkg.dev/sillyprojectid/notarepository/testimage:v1",
            force=True,
        )

    def test_bad_copy_env(self):
        """Test tries to copy env to remote environment, but fails to do so due to faulty path"""
        self.assertRaises(
            BadCopyEnvException,
            build_image,
            "meow:v1",
            "clonebuildregister/test",
            "clonebuildregister/test/buildImageTest.env",
            "sillygoofy/!~",
        )

    def test_cbr_exception_del_repository_clone_name(self):
        """Test shows CBR exception,"""

        self.assertRaises(
            CBRException,
            clonebuildregister,
            GITHUB_REPO_ORG,
            GITHUB_REPO_NAME,
            GITHUB_REPO_BRANCH,
            "testimage",
            "v1",
            "funny",
            "testimage",
            "v1",
            "sillylocation",
            "notgood",
            f"{GCLOUD_REPOSITORY}",
            delete_repository=True,
            clone_name="funny",
        )
        client = docker.from_env()
        self.assertTrue(len(client.images.list(name="testimage")) > 0)

        self.assertFalse(os.path.exists("funny"))

    def test_cbr_exception_del_repository(self):
        """Test shows CBR exception,"""

        self.assertRaises(
            CBRException,
            clonebuildregister,
            GITHUB_REPO_ORG,
            GITHUB_REPO_NAME,
            GITHUB_REPO_BRANCH,
            "testimage",
            "v1",
            GITHUB_REPO_NAME,
            "testimage",
            "v1",
            "sillylocation",
            "notgood",
            f"{GCLOUD_REPOSITORY}",
            delete_repository=True,
        )
        client = docker.from_env()
        self.assertTrue(len(client.images.list(name="testimage")) > 0)

        self.assertFalse(os.path.exists(GITHUB_REPO_NAME))
