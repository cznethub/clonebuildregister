#! /usr/bin/env python

"""
A __main__ namespace for the bimage.tests subpackage.
"""

import unittest
from bimage.test import test_cloneRepo
from bimage.test import test_buildImage

if __name__ == "__main__":
    unittest.main(test_cloneRepo)
    
    