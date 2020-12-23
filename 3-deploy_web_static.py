#!/usr/bin/python3
""" Distributes an archive to your
web servers, using the function do_deploy: """

from fabric.api import *
from os import path
import time

env.hosts = ['35.237.110.243', '35.237.226.73']


def do_deploy(archive_path):
    """Deploy in the servers"""
    if path.exists(archive_path) is False:
        return False

    ufile = put(archive_path, '/tmp/')
    if ufile.failed:
        return False

    complete = archive_path.split("/")[-1]
    fileok = complete.split(".")[0]

    run("sudo mkdir -p /data/web_static/releases/{}/".format(fileok))
    run("sudo tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".
        format(fileok, fileok))

    run("sudo rm /tmp/{}.tgz".format(fileok))

    run("sudo mv /data/web_static/releases/{}/web_static/* "
        "/data/web_static/releases/{}/".format(fileok, fileok))
    run("sudo rm -rf /data/web_static/releases/{}/web_static".
        format(fileok))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current".
        format(fileok))
    return True


def do_pack():
    """ Generates .tgz """

    local("mkdir -p versions")
    created = (time.strftime("%Y%m%d%H%M%S"))
    tgzfile = local("tar -cvzf versions/web_static_{}.tgz web_static"
                    .format(created))
    if not tgzfile.succeeded:
        return None
    else:
        return "versions/web_static_{}.tgz".format(created)


def deploy():
    """Deploys all"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
