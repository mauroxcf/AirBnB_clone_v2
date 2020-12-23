#!/usr/bin/python3
""" Fabric module generates a .tgz archive"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    generates a .tgz archive from the contents
     of the web_static folder
    """
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d%H%M%S")
    try:
        local ("mkdir -p versions")
        local("tar -zcvf versions/web_static_{}.tgz web_static/".format(dt_string))
        return ("versions/{}.tgz".format(compress))

    except:

        return None
