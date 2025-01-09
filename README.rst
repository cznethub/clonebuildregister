CloneBuildRegister Usage
=========================

CloneBuildRegister
-------------------

Clones a repository, builds a docker image from that repository, and then pushes that image to Google Cloud Artifact Registry.

To use CloneBuildRegister as a package:

.. code-block:: python

   from clonebuildregister.clonebuildregister import clonebuildregister
   clonebuildregister("cbcunc", "timage", "develop", "testimage", "v1", "timage", "testimage", "v1", "us-east1", "bimage-project", "bimage-repository")

To use CloneBuildRegister as a script:

.. code-block:: bash

   usage: clonebuildregister [-h] [-v] [-l PATH_TO_LOCAL_ENVIRONMENT] [-r PATH_TO_REMOTE_ENVIRONMENT] [-p PLATFORM] [-cn CLONE_NAME] [-dr DELETE_REPOSITORY] [-di DELETE_ALL_DOCKER_IMAGES]
                             github_org repo_name branch_or_tag local_image_name local_image_tag path_to_dockerfile target_image_name target_image_tag region gcloudProjectId repositoryName

   positional arguments:
     github_org             The GitHub organization of the repository
     repo_name              The name of the repository in the organization
     branch_or_tag          The branch or tag of the repository
     local_image_name       The name of the image we create locally from the Dockerfile
     local_image_tag        The tag of the image we create locally from the Dockerfile (v1, 1.0.1, version2.0)
     path_to_dockerfile     The path to the docker file from the repository we cloned, usually the name of the repository
     target_image_name      The target image name, i.e., the name of the image we store in the Google Cloud Artifact Registry
     target_image_tag       The target image tag, i.e., the tag of the image we store in the Google Cloud Artifact Registry (v1, 1.0.1, version2.0)
     region                 Region the image will be stored in the Google Cloud (e.g., us-east1, us, eu)
     gcloudProjectId        The project id under which the image will be stored in a Google Artifact Registry
     repositoryName         The name of the Google Cloud Artifact Registry that holds Docker images

   options:
     -h, --help            show this help message and exit
     -v, --version         show program's version number and exit
     -l PATH_TO_LOCAL_ENVIRONMENT, --path_to_local_environment PATH_TO_LOCAL_ENVIRONMENT
                           The path to a local environment file with secrets not to be seen on GitHub (e.g., usr/home/clonebuildregister/.env). Defaults to . (default: )
     -r PATH_TO_REMOTE_ENVIRONMENT, --path_to_remote_environment PATH_TO_REMOTE_ENVIRONMENT
                           The path to the dummy environment files found on GitHub (e.g., usr/home/clonebuildregister/.env). Defaults to . (default: )
     -p PLATFORM, --platform PLATFORM
                           The target platform of the image in the form of os[/arch[/variant]] (default: )
     -cn CLONE_NAME, --clone_name CLONE_NAME
                           The name of the top-level folder of the GitHub repository after cloning. (default: )
     -dr DELETE_REPOSITORY, --delete_repository DELETE_REPOSITORY
                           Boolean that tells the program to delete the GitHub repository that it clones after it registers it to the Google Cloud AR (default: False)
     -di DELETE_ALL_DOCKER_IMAGES, --delete_all_docker_images DELETE_ALL_DOCKER_IMAGES
                           Boolean that tells the program to delete all Docker images on the local system after the program puts the image on the Google Cloud Artifact Registry. Deletes using force. Similar to running
                           $ docker rmi -f $(docker images -aq) (default: False)

   example:
       $ python -m clonebuildregister cbcunc timage develop testimage v1 timage testimage v1 us-east1 bimage-project bimage-repository

Module Usage
============

Use the module ``buildImage``:

.. code-block:: python

   from clonebuildregister.buildImage import buildImage
   image = buildImage("testimage:v1", "") # if Dockerfile in current directory, use 2nd argument as target directory

Use the module ``cloneRepo``:

.. code-block:: python

   from clonebuildregister.cloneRepo import cloneRepo
   cloneRepo("cbcunc", "timage", "develop") # github_org, repo_name, branch_or_tag

Use the module ``cloneRepo`` with environment variable copy:

.. code-block:: python

   from clonebuildregister.cloneRepo import cloneRepo
   cloneRepo("cbcunc", "timage", "develop", "path_to_secrets", "path_in_repo_to_env_file") # github_org, repo_name, branch_or_tag

Use the module ``registerImage``:

.. code-block:: python

   # Don't forget to authenticate to gcloud within your shell before trying this command
   from clonebuildregister.registerImage import registerImage
   response = registerImage("testimage", "v2", "test-image-out", "v1", "us-east1", "bimage-project", "bimage-repository")

How to configure clonebuildregister with gcloud as a developer
===============================================================

1. Create an account with Google Cloud at https://cloud.google.com
2. Create a new project called bimage-project.
3. Go to the Google Cloud Artifact Registry and create a repository called bimage-repository; ensure the repository zone is ``us-east1``.
4. From there, go to the terminal where you cloned ``bimage`` and ensure you have the gcloud CLI installed: https://cloud.google.com/sdk/docs/install.
5. Make sure to add to path and run ``gcloud init``, ensuring you choose ``bimage-project``.
6. Also ensure to run ``gcloud auth login``, if needed.
7. Make sure ``cat ~/.docker/config.json`` contains ``us-east1``. If not, run ``gcloud auth configure-docker us-east1-docker.pkg.dev`` to add it.
8. The test cases should now work assuming you also have Docker running in the background and have already run ``python setup.py develop``.

Install Python Dependencies
===========================

1. Navigate to ``clonebuildregister`` top-level folder.
2. Create a Python environment so that your default environment doesn't get cluttered.
3. Install dependencies using ``pip install .`` (doesn't include ``pytest`` or ``tox``; see "Run Tests" section for that).
4. Ensure you have Docker installed.

Run Tests
=========

1. Navigate to ``clonebuildregister`` top-level folder.
2. Ensure you have Google Cloud, Docker, and the required dependencies.
3. Make sure ``clonebuildregister/test/testing_variables.py`` has the correct values for the setup you have.
4. ``pip install -e '.[dev]'``
5. Run ``pytest`` to run tests in local environment.
6. Run ``tox`` to run tests for Python environments 3.8, 3.9, 3.10, 3.11, and 3.12, along with linting, type checking, and style checking.
7. Run ``tox -e style`` to just do style checking.
8. ``tox -e lint`` for just linting.
9. ``tox -e type`` for just type checking.

