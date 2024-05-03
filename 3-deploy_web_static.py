#!/usr/bin/python3
"""Creates and distributes an archive to your web servers"""

import os
from datetime import datetime as time
from fabric.api import env, run, put, local


env.hosts = ['54.197.44.154', '52.23.212.226']
env.user = 'ubuntu'
CHARS = [':', '-', '.', ' ']


def archived_folder_name():
    """creates an archived file with the following format
        folder format web_static_<year><month><day><hour><minute><seconds>.tgz
    """
    tnow = str(time.now())
    for ch in CHARS:
        if (tnow.find(ch)):
            tnow = tnow.replace(ch, "")
    archive_name = "web_static_{}.tgz".format(tnow)
    return archive_name


def do_pack() -> str:
    """Creating a new archive from all the web_static files"""
    archive_name = archived_folder_name()
    local('mkdir -p versions')
    local('tar -cvzf versions/%s' % archive_name)
    size = os.stat('versions/{}'.format(archive_name)).st_size
    print("web_static packed: versions/{} -> {}".format(archive_name, size))
    return (archive_name)


def do_deploy(archive_path) -> bool:
    """Takes the archived file then uncompress it on the remote servers"""
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
            run("mv /data/web_static/releases/{}/web_static/* \
                    /data/web_static/releases/{}"
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


def deploy() -> bool:
    """Function that makes a call to both of the function do_pack and do_deploy"""
    full_path = do_pack()

    if (not os.path.exists(full_path)):
        return False

    file_deployed = do_deploy(full_path)
    return (file_deployed)
