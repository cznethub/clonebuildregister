#! /usr/bin/env python

"""
A __main__ namespace for the bimage package.
"""

import sys
import argparse
from cloneRepo import cloneRepo


def main(argv):
    """
    Call bimage when the package is run as a script.

    usage: bimage [-h] github_org repo_name branch_or_tag

    positional arguments:
        github_org     The GitHub organization of the repository
        repo_name      The name of the repository in the organization
        branch_or_tag  The branch or tag of the repository

    options:
        -h, --help     show help message and exit
    """

    parser = argparse.ArgumentParser(prog='bimage',
                                     description='Build a container image described in a GitHub repository.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("github_org",
                        help="The GitHub organization of the repository")
    parser.add_argument("repo_name",
                        help="The name of the repository in the organization")
    parser.add_argument("branch_or_tag",
                        help="The branch or tag of the repository")
    args = parser.parse_args(argv)
    cloneRepo(args.github_org, args.repo_name, args.branch_or_tag)


if __name__ == '__main__':
    main(sys.argv[1:])