#!/usr/bin/python3
"""Fabric script to distribute an archive to web servers"""

from fabric.api import env, put, run, local
from os.path import exists
from datetime import datetime

env.hosts = ['18.233.62.201', '100.26.164.127']
env.user = 'ubuntu'
env.key_filename = '/AirBnb_clone_v2/my_key'


def do_pack():
    """Compress the contents of web_static folder"""
    now = datetime.now()
    file_name = "web_static_{}.tgz".format(
        now.strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    result = local("tar -cvzf versions/{} web_static".format(file_name))
    if result.failed:
        return None
    return "versions/{}".format(file_name)


def do_deploy(archive_path):
    """Distribute an archive to web servers"""
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, "/tmp/")

        # Create directory for the new release
        release_folder = "/data/web_static/releases/{}".format(
            archive_path.split("/")[-1][:-4])
        run("mkdir -p {}".format(release_folder))

        # Uncompress the archive to the release folder
        run("tar -xzf /tmp/{} -C {}".format(
            archive_path.split("/")[-1], release_folder))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(archive_path.split("/")[-1]))

        # Move contents of web_static to the release folder
        run("mv {}/web_static/* {}".format(
            release_folder, release_folder))

        # Remove the now empty web_static directory
        run("rm -rf {}/web_static".format(release_folder))

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link to the new release
        run("ln -s {} /data/web_static/current".format(release_folder))
        return True
    except Exception as e:
        return False
