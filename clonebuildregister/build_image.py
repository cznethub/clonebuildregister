#! /usr/bin/env python

"""
This module builds an image via dockerpy
"""

import shutil

from pprint import pprint
import threading
import docker
from dotenv import dotenv_values

from clonebuildregister.exceptions import BadCopyEnvException
from clonebuildregister.exceptions import BuildImageException


def build_image(name: str, target: str, path_to_local_environment: str = "",
                path_to_remote_environment: str = "", platform: str = ""):
    """The build image function.

    Args:
        name (str): The name of the image we are trying to build
        target (str): The path that contains the dockerfile we want to build,
            "." for current directory. If clone_name used, insert "{clone_name}/..." to find Dockerfile
        path_to_local_environment (str, optional): The path to a local environment
                file with secrets not to be seen on github (e.g usr/home/clonebuildregister/.env).
                Defaults to "".
        path_to_remote_environment (str, optional): The path to the dummy environment
                files found on github (e.g usr/home/clonebuildregister/.env). Defaults to "".
        platform (str, optional): The target platform in the format os[/arch[/variant]].

    Returns:
        Image: Returns image object that was built by this function
    """

    if (path_to_local_environment and path_to_remote_environment):
        env_values = dotenv_values(path_to_local_environment)
        try:
            shutil.copyfile(path_to_local_environment, path_to_remote_environment)
        except Exception as exc:
            raise BadCopyEnvException(path_to_local_environment, path_to_remote_environment) from exc
    if (path_to_local_environment and not path_to_remote_environment):
        env_values = dotenv_values(path_to_local_environment)
    else:
        env_values = dotenv_values(".env")
    
    client = docker.APIClient(base_url='unix://var/run/docker.sock') #could be problem statement, could mess up the portability.
    # events = client.events()
    # threading.Thread(target=log_events_helper, name="log_events_helper", args=(client,)).start()
    response = ""
    try:
        if platform:
            response = [line for line in client.build(
                rm=True,
                path=f"./{target}/",
                tag=name,
                buildargs=dict(env_values),
                platform=platform,
                decode=True
            )]
            
            pprint(response)
        else:
            
            
            response = [line for line in client.build(
                rm=True,
                path=f"./{str(target)}/",
                tag=name,
                buildargs=dict(env_values),
                decode=True
            )]
            
            
            pprint(response)
        # gets you docker output.
        # for item in image[1]:
        #     for key, value in item.items():
        #         if key == 'stream':
        #             text = value.strip()
        #             if text:
        #                 print(text)
    except Exception as exc:
        
        raise BuildImageException from exc
    
    return response


# Not used since events don't trigger on failure
# def log_events_helper(client):
#     """
#     Helper to log events through Docker.
#     @param events the event object that docker py created to help print logs
#     """
#     print("got here")
#     i =0
#     events = client.events()
#     for event in events:
#         i +=1
#         print(i)
#         pprint(event)
#     print("it's ended")
