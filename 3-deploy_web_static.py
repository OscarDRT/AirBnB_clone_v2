#!/usr/bin/python3

from fabric.api import local, runs_once, env, put, run
from os import stat, path
from datetime import datetime


file_path = None
env.hosts = ["35.227.22.206", "34.235.89.220"]


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


def do_deploy(archive_path):
    try:
        stat(archive_path)
    except:
        return False
    try:
        name = archive_path.split("/")
        name = name[1].split(".")
        name = name[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(name))
        run("tar -xzf /tmp/{}.tgz -C \
            /data/web_static/releases/{}/".format(name, name))
        run("rm /tmp/{}.tgz".format(name))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ \
            /data/web_static/current".format(name))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """deployment"""
    global file_path
    if file_path is None:
        file_path = do_pack()
    if file_path is None:
        return False
    return do_deploy(file_path)
