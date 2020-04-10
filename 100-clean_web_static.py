#!/usr/bin/python3

from fabric.api import local, run, env
from os import path

env.hosts = ["35.227.22.206", "34.235.89.220"]


def do_clean(number=0):
    number = int(number)
    if number < 0:
        return
    if number == 0 or number == 1:
        number = 1
    loc = local("ls -t versions/", capture=True)
    loc = str(loc)
    if loc == "":
        return
    loc = loc.split("\n")
    n = len(loc)
    for i in range(number, n):
        local("rm versions/{}".format(loc[i]))
        name = loc[i].split(".")
        name = name[0]
        run("rm -rf /data/web_static/releases/{}/".format(name))
