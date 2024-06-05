"""
Exception module, that hold all custom exceptions this program utilizes for better use
"""


class GCloudRegisterImageException(Exception):
    """Exception raised when registering image to google cloud fails"""

    def __init__(
        self,
        message="Check region, project id, and repository name. If those are not causing\
                  the issue then try gcloud init or check if network is causing the issue.",
    ):
        self.message = message
        super().__init__(self.message)


class BadCopyEnvException(Exception):
    """Exception raised for errors when cloning a repository from GitHub

    Attributes:
        source_path -- input source path that caused the error
        target_path  -- input target path that caused the error
        message -- explanation of the error
    """

    def __init__(
        self,
        source_path,
        target_path,
        message="Copy of env failed (check source and target path)",
    ):
        self.source_path = source_path
        self.target_path = target_path
        self.message = message
        super().__init__(self.message)


class BuildImageException(Exception):
    """Exception raised for errors when building an image

    Attributes:
        message -- explanation of the error
    """

    def __init__(
        self,
        message="Building image has failed. Try docker build cli for better error messages",
    ):
        self.message = message
        super().__init__(self.message)


class TagImageException(Exception):
    """Exception raised for errors when tagging an image before registering \
        it gcloud artifact registry

    Attributes:
        message -- explanation of the error
    """

    def __init__(
        self,
        message="Error tagging image before registering it to gcloud artifact registry. \
                    Check local_image_tag is correct.",
    ):
        self.message = message
        super().__init__(self.message)


class CloneRepositoryException(Exception):
    """Exception raised for errors when building an image

    Attributes:
        message -- explanation of the error
    """

    def __init__(
        self,
        message="Cloning repo has failed. Check arguments pertaining to github repos",
    ):
        self.message = message
        super().__init__(self.message)


class CBRException(Exception):
    """Exception raised for errors when cloning a repo, building an image, and posting it to gcloud

    Attributes:
        message -- explanation of the error
    """

    def __init__(
        self,
        message="Something has gone wrong running clonebuildregister, check params",
    ):
        self.message = message
        super().__init__(self.message)
