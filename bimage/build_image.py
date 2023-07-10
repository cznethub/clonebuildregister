#! /usr/bin/env python

"""
This module builds an image via dockerpy
"""
# Standard lib
import shutil

# Third party
import docker
from dotenv import load_dotenv

# Local
from bimage.exceptions import BadCopyEnvException


def build_image(name: str, target: str, path_to_local_environment: str = "",
                path_to_remote_environment: str = ""):
    """The build image function.

    Args:
        name (str): The name of the image we are trying to build
        target (str): The path that contains the dockerfile we want to build,
            "." for current directory
        path_to_local_environment (str, optional): The path to a local environment
                file with secrets not to be seen on github (e.g usr/home/bimage/.env).
                Defaults to "".
        path_to_remote_environment (str, optional): The path to the dummy environment
                files found on github (e.g usr/home/bimage/.env). Defaults to "".

    Returns:
        Image: Returns image object that was built by this function
    """

    if (path_to_local_environment and path_to_remote_environment):
        load_dotenv(dotenv_path=path_to_local_environment)
        try:
            shutil.copyfile(path_to_local_environment, path_to_remote_environment)
        except BadCopyEnvException(path_to_local_environment, path_to_remote_environment) as exc:
            print(exc)
    if (path_to_local_environment and not path_to_remote_environment):
        load_dotenv(dotenv_path=path_to_local_environment)
    else:
        load_dotenv()
    client = docker.from_env()
    image = client.images.build(
        rm=True,
        path=f"./{target}/",
        tag={name}
    )
    return image
