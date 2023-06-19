#! /usr/bin/env python

"""
Setup script for the bimage package.
"""

from setuptools import setup
from setuptools import find_packages


def version():
    """Get the version number."""

    with open("VERSION.txt") as v:
        _version = v.read()
    return _version.strip()


__version__ = version()


def long_description():
    """Construct the long description text."""

    with open("README.rst") as r:
        long_description_1 = r.read()
    with open("HISTORY.txt") as h:
        long_description_2 = h.read()
    return "\n".join([long_description_1, long_description_2, ])


setup(name="bimage",
      version=__version__,
      license="BSD3",
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      author="Chris Calloway",
      author_email="cbc@chriscalloway.org",
      description="Model package for building container images",
      long_description=long_description(),
      url="https://github.com/cbcunc/bimage",
      download_url="https://github.com/cbcunc/bimage/tarball/" + __version__,
      keywords="docker image build",
      classifiers=["Development Status :: 1 - Planning",
                   "License :: OSI Approved :: BSD License",
                   "Programming Language :: Python :: 3",
                   "Topic :: Software Development :: Build Tools",
                   ],
      zip_safe=False,
      test_suite="bimage.tests",
      scripts=[
            'bimage/cloneRepo.py'
              ]
    )