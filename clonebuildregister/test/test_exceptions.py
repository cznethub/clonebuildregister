#! /usr/bin/env python

"""
Tests for the bimage module.
"""
import unittest
from clonebuildregister.clone_repo import clone_repo
from clonebuildregister.build_image import build_image
from clonebuildregister.register_image import register_image
from clonebuildregister.exceptions import CloneRepositoryException
from clonebuildregister.exceptions import BuildImageException
from clonebuildregister.exceptions import TagImageException


class TestExceptions(unittest.TestCase):
    """Test registerImage in the bimage module. Relies on buildImage"""

    def test_clone_repo_fail(self):
        """This test tries throwing exception on clone_repo 
        """
        self.assertRaises(CloneRepositoryException, clone_repo, "meow", \
                          "this_repo_don'texists", "1232132tttt") 


    def test_build_image_fail(self):
        """This test tries throwing exception on build_image 
        """
        self.assertRaises(BuildImageException, build_image, "meow", "/asdfasdf/adsf")


    def test_register_image_fail(self):
        """ Test tries building a faulty image"""
        self.assertRaises(TagImageException, register_image, "ruff12", "v12", "rufff12", \
                          "v12", "idkwhere", "this_is_notaproject","funnynamehere")



if __name__ == "__main__":
    unittest.main()
