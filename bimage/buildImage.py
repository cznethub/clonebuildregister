#! /usr/bin/env python

"""
This module builds an image via dockerpy
"""

import docker
import shutil
from bimage.exceptions import badCopyEnvException
def buildImage(name: str, target: str, path_to_local_environment: str="", path_to_remote_environment: str=""):
    """
        The build image function.

        Parameters:
            name              The name of the image we are trying to build
            target            The path that contains the dockerfile we want to build, "." for current directory
            path_to_local_environment (str, optional):  The path to a local environment file with secrets not to be seen on github (e.g usr/home/bimage/.env).. Defaults to "".
            path_to_remote_environment (str, optional): The path to the dummy environment files found on github (e.g usr/home/bimage/.env). Defaults to "".
        Returns: image, the image that was built.
    """
    
    if (path_to_local_environment and path_to_remote_environment):
        try:
            shutil.copyfile(path_to_local_environment, path_to_remote_environment)
        except badCopyEnvException:
            raise(badCopyEnvException(path_to_local_environment, path_to_remote_environment))
            
    
    client = docker.from_env()
    # print(os.getcwd())
    image = client.images.build(
        rm=True,
        path="./{}/".format(target),
        tag={"{}".format(name)}
    )
    return image