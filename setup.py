#! /usr/bin/env python

"""
Setup script for the clonebuildregister package.
"""

from setuptools import setup
from setuptools import find_packages


def version():
    """Get the version number."""

    with open("VERSION.txt", encoding='UTF-8') as version_fd:
        _version = version_fd.read()
    return _version.strip()


__version__ = version()





def long_description():
    """Construct the long description text."""

    with open("README.rst", encoding='UTF-8') as readme_fd:
        long_description_1 = readme_fd.read()
    with open("HISTORY.txt", encoding='UTF-8') as history_fd:
        long_description_2 = history_fd.read()
    return "\n".join([long_description_1, long_description_2, ])



setup(name="clonebuildregister",
      version=__version__,
      license="BSD3",
      packages=find_packages(exclude=["*.test", "*.test.*", "test.*", "test"]),
      author="Jude Sproul",
      author_email="jnsproul@ncsu.edu",
      description="Model package for building container images and posting them to google cloud artifact registry",
      long_description=long_description(),
      long_description_content_type="text/x-rst",
      url="https://github.com/cznethub/clonebuildregister",
      download_url="https://github.com/cznethub/clonebuildregister/tarball/" + __version__,
      keywords="docker image build",
      classifiers=["Development Status :: 1 - Planning",
                   "License :: OSI Approved :: BSD License",
                   "Programming Language :: Python :: 3",
                   "Topic :: Software Development :: Build Tools",
                   ],
      zip_safe=False,
      test_suite="clonebuildregister.test",
      install_requires=["docker"
  ,"gitpython"
  ,"github3.py"
  ,"python-dotenv"
  ,"google-cloud-artifact-registry"
  ,"grpcio-status"]
      )
