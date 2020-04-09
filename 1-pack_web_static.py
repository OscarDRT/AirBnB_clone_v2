#!/usr/bin/python3

from fabric.api import local, runs_once
from os import stat, path
from datetime import datetime


@runs_once
def do_pack():
    try:
        stat("versions")
    except:
        local("mkdir versions")

    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        name = "versions/web_static_{}.tgz".format(time)
        print("Packing web_static to versions/{}".format(name))
        local("tar -cvzf {} web_static".format(name))
        file_size = path.getsize(name)
        print("web_static packed: versions/{} -> \
            {}Bytes".format(name, file_size))
        return name
    except:
        return None
