"""
Exception module, that hold all custom exceptions this program utilizes for better use
"""


class BadCopyEnvException(Exception):
    """Exception raised for errors when cloning a repository from GitHub

    Attributes:
        source_path -- input source path that caused the error
        target_path  -- input target path that caused the error
        message -- explanation of the error
    """

    def __init__(self, source_path, target_path,
                 message="Copy of env failed (check source and target path)"):
        self.source_path = source_path
        self.target_path = target_path
        self.message = message
        super().__init__(self.message)
