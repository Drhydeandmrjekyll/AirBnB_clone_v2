#!/usr/bin/python3
"""
This script deploys a web application to web servers using Fabric.
"""

from fabric.api import env, local, put, run
from datetime import datetime
import os

# Define the user and SSH key (customize as needed)
env.user = 'ubuntu'
env.key_filename = '/AirBnB_clone_v2/my_key'

# Define the IP addresses of your web servers
env.hosts = ['18.233.62.201', '100.26.164.127']

def do_pack():
    """
    Create a compressed archive of the web_static folder.

    Returns:
        str: Path to the archive on success, None on failure.
    """
    try:
        # Create a directory to store the archive
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        archive_path = 'versions/web_static_{}.tgz'.format(timestamp)

        # Create the archive using tar
        local('mkdir -p versions')
        local('tar -czvf {} web_static'.format(archive_path))

        return archive_path
    except Exception as e:
        return None

def do_deploy(archive_path):
    """
    Deploy the web application on the web servers.

    Args:
        archive_path (str): Path to the archive to deploy.

    Returns:
        bool: True on success, False on failure.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the server
        put(archive_path, '/tmp/')

        # Create a directory for the new version
        release_path = '/data/web_static/releases/{}'.format(
            os.path.basename(archive_path).replace('.tgz', '')
        )
        run('mkdir -p {}'.format(release_path))

        # Extract the archive into the new version directory
        run('tar -xzf /tmp/{} -C {}'.format(
            os.path.basename(archive_path), release_path
        ))

        # Delete the archive from the server
        run('rm /tmp/{}'.format(os.path.basename(archive_path)))

        # Move the contents to the current symlink
        run('mv {}/web_static/* {}/'.format(release_path, release_path))

        # Remove the web_static directory in the new version
        run('rm -rf {}/web_static'.format(release_path))

        # Update the symbolic link to the new version
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(release_path))

        return True
    except Exception as e:
        return False

def deploy():
    """
    Deploy the web application to the web servers.

    Returns:
        bool: True on success, False on failure.
    """
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)
