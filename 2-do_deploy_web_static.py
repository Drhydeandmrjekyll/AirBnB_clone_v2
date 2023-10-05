#!/usr/bin/python3
"""
This script deploys a web static archive to web servers.
"""

from fabric.api import env, put, run
import os

# Set your Fabric environment variables here
env.hosts = ['18.233.62.201', '100.26.164.127']

def do_deploy(archive_path):
    """
    Deploy a web static archive to web servers.

    Args:
        archive_path (str): The path to the archive file.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    if not os.path.isfile(archive_path):
        return False

    try:
        # Your deployment logic here
        # ...

        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False

if __name__ == "__main__":
    # You can add code here to call the do_deploy function with the archive path.
