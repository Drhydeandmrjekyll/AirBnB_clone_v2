#!/usr/bin/python3
"""
Fabric script to delete out-of-date archives
"""

from fabric.api import local, env, run, lcd
from datetime import datetime
import os

env.hosts = ['18.233.62.201', '100.26.164.127']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/my_key'


def do_clean(number=0):
    """
    Deletes out-of-date archives from web servers.

    Args:
        number (int): The number of archives to keep.

    """
    if int(number) < 2:
        number = 1
    else:
        number = int(number)

    archives_dir = "/data/web_static/releases"
    with lcd("versions"):
        local_command = "ls -1t | tail -n +{} | xargs -I {{}} rm -f {{}}"
        local_command = local_command.format(number + 1)
        local(local_command)

    with cd(archives_dir):
        remote_command = "ls -1t | tail -n +{} | xargs -I {{}} rm -rf {{}}"
        remote_command = remote_command.format(number + 1)
	run(remote_command)
