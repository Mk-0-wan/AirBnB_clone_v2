#!/usr/bin/env python3
"""Another python fabric file"""

import os
from fabric.api import local
from datetime import datetime as time


CHARS=[':', '-', '.', ' ']


def archived_folder_name():
    """creates the folder name according to the alx style required"""
    tnow = str(time.now())
    for ch in CHARS:
        if (tnow.find(ch)):
            tnow = tnow.replace(ch, "")
    # folder format web_static_<year><month><day><hour><minute><seconds>.tgz
    archive_name = "web_static_{}.tgz".format(tnow)
    return archive_name

def do_pack():
    """Creating a new archive from all the web_static files"""
    archive_name = archived_folder_name()
    local('mkdir -p versions')
    local('tar -cvzf versions/%s' % archive_name)
    size = os.stat('versions/{}'.format(archive_name)).st_size
    print("web_static packed: versions/{} -> {}".format(archive_name, size))
