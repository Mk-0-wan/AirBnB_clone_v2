#!/usr/bin/env python3
"""Fabric deploying script that distributes the archive files to my webservers."""

import os
from fabric.api import env, run, put

env.hosts = ['54.197.44.154', '52.23.212.226']
env.user = "ubuntu"

def do_deploy(archive_path) -> bool:
    """uploads the archived files, uncompress them then distributes them"""
    if (not os.path.exists(archive_path)):
        return False
    else:
        try:
            new_path = archive_path.split("/")[1]
            new_folder = new_path.replace(".tgz", "")

            put("{}".format(archive_path), "/tmp/{}".format(new_path))
            run(" mkdir -p /data/web_static/releases/{}".format(new_folder))
            run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}"
                .format(new_folder, new_folder))
            run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}"
                .format(new_folder, new_folder))
            run("rm -rf /data/web_static/releases/{}/web_static"
                .format(new_folder))
            run("rm -rf /data/web_static/current")
            run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
                .format(new_folder))
        except Exception:
            return False
        print("New version deployed!")
        return True
