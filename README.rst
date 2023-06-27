# bimage
Building an image in Python using docker and github3 packages


usage: bimage [-h]
              github_org repo_name branch_or_tag local_image_name local_image_tag path_to_dockerfile target_image_name
              target_image_tag region gcloudProjectId repositoryName

Build a container image described in a GitHub repository and push that image to google cloud artifact registry.

positional arguments:
  github_org          The GitHub organization of the repository
  repo_name           The name of the repository in the organization
  branch_or_tag       The branch or tag of the repository
  local_image_name    The name of the image we create locally from the Dockerfile
  local_image_tag     The tag of the image we create locally from the Dockerfile (v1, 1.0.1, version2.0)
  path_to_dockerfile  The path to the docker file from the repository we cloned, usually the name of the repository
  target_image_name   The target image name, i.e. the name of the image we store in the google cloud artifact registry
  target_image_tag    The target image tag, i.e. the tag of the image we store in the google cloud artifact registry (v1,
                      1.0.1, version2.0)
  region              Region the image will be stored in the google cloud (e.g. us-east1, us, eu)
  gcloudProjectId     The project id from which the image will be stored under in a google artifact registry
  repositoryName      The name of the google cloud artifact registry that holds docker images

options:
  -h, --help          show this help message and exit