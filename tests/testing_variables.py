"""
    Provides one place where developers can change variable names
    for entire test-suite. Currently only includes things related
    to google cloud.
"""

GCLOUD_PROJECT = "cznet-393818"
GCLOUD_REPOSITORY = "cbr-testing"

GCLOUD_LOCATION = "us-east1"

# Everything for cloning the test github repo
# that contains a working docker file named bimage
# using continuumio/miniconda3:latest, as base
GITHUB_REPO_ORG = "cbcunc"
GITHUB_REPO_NAME = "timage"
GITHUB_REPO_BRANCH = "develop"
