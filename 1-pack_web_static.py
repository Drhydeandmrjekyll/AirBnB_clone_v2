#!/usr/bin/python3
"""Fabric script to generate a .tgz archive from web_static folder."""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    "Create a .tgz archieve from webstatic folder."""
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(current_time)
        web_static_path = "/home/ubuntu/AirBnB_clone_v2/web_static"

        if not os.path.exists("versions"):
            os.mkdir("versions")

        local("tar -czvf {} {}".format(archive_name, web_static_path))

        if os.path.exists(archive_name):
            return archive_name

    except Exception as e:
        return None
