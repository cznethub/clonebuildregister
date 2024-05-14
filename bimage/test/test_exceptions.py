#! /usr/bin/env python

"""
Tests for the bimage module.
"""
import unittest
from bimage.clone_repo import clone_repo
from bimage.build_image import build_image
from bimage.register_image import register_image
from bimage.exceptions import CloneRepositoryException
from bimage.exceptions import BuildImageException
from bimage.exceptions import TagImageException


class TestExceptions(unittest.TestCase):
    """Test registerImage in the bimage module. Relies on buildImage"""

    def test_clone_repo_fail(self):
        """This test tries throwing exception on clone_repo 
        """
        self.assertRaises(Exception, clone_repo, "meow", "this_repo_don'texists", "1232132tttt") # SHould be CloneRepositoryException here instead of generic
        # try:
        #     clone_repo("meow", "this_repo_don'texists", "1232132tttt")
        # except CloneRepositoryException as exc:
        #     self.assertEqual(exc.message, "Cloning repo has failed. \
        #                      Check arguments pertaining to github repos")

    def test_build_image_fail(self):
        """ Test tries building a faulty image"""
        self.assertRaises(Exception, build_image, "meow", ".")
        # try:
        #     build_image("meow", ".")  # there is no dockerfile in this directory
        # except Exception as exc: # BuildImageException instead here
        #     self.assertEqual(exc.message, "Building image has failed. \
        #                      Try docker build cli for better error messages")

    def test_register_image_fail(self):
        """ Test tries building a faulty image"""
        self.assertRaises(Exception, register_image, "v12", "rufff12", "v12", "idkwhere", "this_is_notaproject",
                           "funnynamehere")
        # try:
        #     register_image("meow1111", "v12", "rufff12", "v12", "idkwhere", "this_is_notaproject",
        #                    "funnynamehere")  # there is no dockerfile in this directory
        # except Exception as exc: # should be TagImageException not generic
        #     self.assertEqual(exc.message, "Error tagging image before \
        #                      registering it to gcloud artifact registry. \
        #             Check local_image_tag is correct.")


if __name__ == "__main__":
    unittest.main()
