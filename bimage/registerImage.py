#! /usr/bin/env python

"""
The registerImage module.
"""

import docker 

def registerImage(localImageName:str, localImageTag:str, targetImageName:str, targetImageTag:str, region:str, gcloudProjectId:str, repositoryName:str):
    """
    The registerImage function.

        Parameters:
            localImageName     The name of the local image that we are going to push to gcloud
            localImageTag      The tag of the local image that we are going to push to gcloud
            targetImageName    The name of the image when it is pushed to gcloud
            targetImageTag     The tag of the image when it is pushed to gcloud, i.e. v1, version2.0, or 1.0.1
            region             Name of gcloud region the repository is at, i.e. us-east1
            gcloudProjectId    The id of the gcloud project that has the artifact registry repository
            repositoryName     The name of the gcloud repository

        Returns: None
    """

    # first the image needs to be tagged
    client = docker.from_env()
    image = client.images.get("{}:{}".format(localImageName, localImageTag))
    image.tag(
        repository = "{}-docker.pkg.dev/{}/{}/{}".format(region, gcloudProjectId, repositoryName, targetImageName),
        tag        = targetImageTag
    )
    response = client.images.push(
        "{}-docker.pkg.dev/{}/{}/{}".format(region, gcloudProjectId, repositoryName, targetImageName),
        tag = targetImageTag
    )
    return response
