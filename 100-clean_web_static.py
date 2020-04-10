#!/usr/bin/python3

from fabric.api import local, run, env
from os import path

env.hosts = ["35.227.22.206", "34.235.89.220"]


def do_clean(number=0):
    number = int(number)
    local("ls -d -1tr versions/* | tail -n +{} | \
          xargs -d '\n' rm -f --".format(2 if number < 1 else number + 1))
    run("ls -d -1tr /data/web_static/releases/* | tail -n +{} | \
          xargs -d '\n' rm -rf --".format(2 if number < 1 else number + 1))
