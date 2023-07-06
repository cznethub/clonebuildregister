#! /usr/bin/env python

"""
The registerImage module.
"""

import docker

def register_image(local_image_name:str, local_image_tag:str, target_image_name:str, 
                  target_image_tag:str, region:str, gcloud_project_id:str, repository_name:str):
    """
    The registerImage function.

        Parameters:
            local_image_name     The name of the local image that we are going to push to gcloud
            local_image_tag      The tag of the local image that we are going to push to gcloud
            target_image_name    The name of the image when it is pushed to gcloud
            target_image_tag     The tag of the image when it is pushed to gcloud, \
                i.e. v1, version2.0, or 1.0.1
            region               Name of gcloud region the repository is at, \
                i.e. us-east1
            gcloud_project_id    The id of the gcloud project that has the artifact \
                registry repository
            repository_name      The name of the gcloud repository

        Returns: None
    """

    # first the image needs to be tagged
    client = docker.from_env()
    image = client.images.get(f"{local_image_name}:{local_image_tag}")
    image.tag(
        repository =
        f"{region}-docker.pkg.dev/{gcloud_project_id}/{repository_name}/{target_image_name}",
        tag        = target_image_tag
    )
    response = client.images.push(
        f"{region}-docker.pkg.dev/{gcloud_project_id}/{repository_name}/{target_image_name}",
        tag = target_image_tag
    )
    return response
