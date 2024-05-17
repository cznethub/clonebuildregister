
******************
clonebuildregister
******************

Clones a repository, builds a docker image from that repository, and then pushes that image to google cloud artifact registry

To use clonebuildregister as a package:

    >>> from clonebuildregister.clonebuildregister import clonebuildregister
    >>> clonebuildregister("cbcunc", "timage", "develop", "testimage", "v1", "timage", "testimage", "v1", "us-east1", "bimage-project", "bimage-repository")
    >>>

To use clonebuildregister as a script:

    usage: python -m clonebuildregister [-h] \
                  github_org repo_name branch_or_tag local_image_name local_image_tag path_to_dockerfile target_image_name \
                  target_image_tag region gcloudProjectId repositoryName
    
    Build a container image described in a GitHub repository and push that image to google cloud artifact registry.
    
    positional arguments:
      ==================  ===================================================================================================
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
      ==================  ===================================================================================================
    
    options:

        - -h, --help          show this help message and exit
        - --l L, -path_to_local_environment L
                        The path to a local environment file with secrets not to be seen on github (e.g usr/home/clonebuildregister/.env). Defaults to .
                        (default: None)
        - --r R, -path_to_remote_environment R
                        The path to the dummy environment files found on github (e.g usr/home/clonebuildregister/.env). Defaults to . (default: None)
        - --p P, -platform P    The target platform of the image in the form of os[/arch[/variant]] (default: None)
    
    example:
        $ python -m clonebuildregister cbcunc timage develop testimage v1 timage testimage v1 us-east1 bimage-project bimage-repository

Use modules of clonebuildregister
*********************************
Use the module buildImage:
    >>> from clonebuildregister.buildImage import buildImage
    >>> image = buildImage("testimage:v1","") # if Dockerfile in current directory, use 2nd argument as target directory
    >>>
Use the module cloneRepo:
    >>> from clonebuildregister.cloneRepo import cloneRepo
    >>> cloneRepo("cbcunc", "timage", "develop") # github_org, repo_name, branch_or_tag
    >>>
Use the module cloneRepo with environment variable copy:
    >>> from clonebuildregister.cloneRepo import cloneRepo
    >>> cloneRepo("cbcunc", "timage", "develop", "path_to_secrets", "path_in_repo_to_env_file") # github_org, repo_name, branch_or_tag
    >>>
Use the module registerImage:
    >>> # don't forget to authenticate to gcloud within your shell before trying this command
    >>> from clonebuildregister.registerImage import registerImage
    >>> response = registerImage("testimage", "v2", "test-image-out", "v1", "us-east1", "bimage-project", "bimage-repository")
    >>> 

How to configure clonebuildregister with gcloud as a developer
**************************************************************
1. Create an account with Google Cloud at https://cloud.google.com 
2. Create a new project called bimage-project
3. Go to the google cloud artifact registry and create a repository called bimage-repository ensure the repository zone is us-east1
4. From there goto the terminal where you cloned bimage and ensure you have the gcloud CLI installed https://cloud.google.com/sdk/docs/install
5. Make sure add to path and run $ gcloud init, ensuring you choose bimage-project
6. Also ensure to run $ gcloud auth login, if needed
7. Make sure $ cat ~/.docker/config.json contains us-east1. If not run $ gcloud auth configure-docker us-east1-docker.pkg.dev to add it.
8. The test cases should now work assuming you also have docker running in the background and have already run $ python setup.py develop

Install python dependencies
***************************
1. Navigate to clonebuildregister top-level folder
2. Create a python environment so that your default environment doesn't get cluttered
3. Run $ conda install --file requirements.txt

Run Tests
*********
1. Navigate to clonebuildregister top-level folder 
2. $ python -m pytest
3. If it doesn't work, do this. Replace all string instances of bimage-project-###### with the project id that you have been given. TODO: make it simpler so that you don't have to do the previous step.
