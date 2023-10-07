#!/usr/bin/python3
"""Fabric script to generate a .tgz archive from web_static folder."""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Create a .tgz archive from the web_static folder."""
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(current_time)
        web_static_path = "web_static"

        if not os.path.exists(web_static_path):
            print("Error: 'web_static' folder does not exist.")
            return None

        local("mkdir -p versions")

        result = local("tar -czvf {} {}".format(archive_name, web_static_path))

        if result.succeeded:
            return archive_name
        else:
            print("Error: Failed to create the archive.")
            return None

    except Exception as e:
        print("Error:", str(e))
        return None


if __name__ == "__main__":
    do_pack()
