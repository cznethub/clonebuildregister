#! /usr/bin/env python

"""
The registerImage module.
"""

from pprint import pprint

import docker
from google.cloud import artifactregistry_v1

# from google.api_core.exceptions import NotFound

from .exceptions import GCloudRegisterImageException
from .exceptions import TagImageException


def register_image(
    local_image_name: str,
    local_image_tag: str,
    target_image_name: str,
    target_image_tag: str,
    region: str,
    gcloud_project_id: str,
    repository_name: str,
    delete_all_docker_images: bool = False,
):
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
    gcloud_client = artifactregistry_v1.ArtifactRegistryClient()
    # get version of current tagged dspback

    gcloud_request = artifactregistry_v1.GetTagRequest(
        name=f"projects/{gcloud_project_id}/locations/{region}/repositories/\
            {repository_name}/packages/{target_image_name}/tags/{target_image_tag}"
    )

    # if no tagged dspback:develop then catch exception
    # google.api_core.exceptions.NotFound: 404 Requested entity was not found.
    gcloud_response = ""
    try:
        gcloud_response = gcloud_client.get_tag(request=gcloud_request)
    except (
        Exception
    ):  # very bad practice, but I want this to work. Exceptions, should be specific.
        gcloud_response = (
            ""  # we really don't care if it breaks or not, we just wanted to
        )
        # know if dspback:devleop exists in the AR
    # which holds response.version

    # first the image needs to be tagged
    client = docker.from_env()
    try:
        image = client.images.get(f"{local_image_name}:{local_image_tag}")
        image.tag(
            repository=f"{region}-docker.pkg.dev/{gcloud_project_id}/{repository_name}/{target_image_name}",
            tag=target_image_tag,
        )
    except Exception as exc:
        raise TagImageException() from exc

    response = client.images.push(
        f"{region}-docker.pkg.dev/{gcloud_project_id}/{repository_name}/{target_image_name}",
        tag=target_image_tag,
    )

    if "errorDetail" in response:
        pprint(response)
        raise GCloudRegisterImageException() from Exception()

    if gcloud_response:
        gcloud_request = artifactregistry_v1.DeleteVersionRequest(
            name=gcloud_response.version, force=True
        )
        gcloud_client.delete_version(request=gcloud_request)
    if delete_all_docker_images:
        print("Attempting to delete remaining local images. Deleting using --force.")
        for image in client.images.list():
            print("Deleting image: ", image.tags)
            client.images.remove(image.id, force=True)
    return response
