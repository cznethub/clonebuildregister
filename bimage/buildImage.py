#! /usr/bin/env python

"""
This module builds an image via dockerpy
"""

import docker
import os

def buildImage(name, target):
    """
        The build image function.

        Parameters:
            name              The name of the image we are trying to build
            target            The path that contains the dockerfile we want to build, "." for current directory

        Returns: image, the image that was built.
    """
    
    client = docker.from_env()
    if (not os.path.exists(target) and not target == ""):
        os.makedirs(target)
    image = client.images.build(
        rm=True,
        path="./{}/".format(target),
        tag={"{}".format(name)}
    )
    return image