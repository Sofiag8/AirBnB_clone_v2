#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from
the contents of the web_static
"""
from time import strftime
from datetime import date
from fabric.api import *
from os import path

env.hosts = ['35.196.158.6', '35.227.106.6']
env.password = 'betty'

def do_pack():
    """
    All files in the folder web_static must be added to
    the final archive.
    All archives must be stored in the folder versions
    (function should create this folder if it doesnt
    exist)
    The name of the archive created must be
    web_static_<year><month><day><hour><minute>
    <second>.tgz
    The function do_pack must return the archive path
    if the archive has been correctly generated.
    Otherwise, it should return None
    """
    timestamp = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{:s}.tgz web_static/"
              .format(timestamp))
        return ("versions/web_static_{:s}.tgz".format(timestamp))
    except:
        return None


def do_deploy(archive_path):
    """
    Returns False if the file at the path archive_path
    doesnt exist
    If it does, deploy!
    """
    if not path.exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        folder_to_compress = ("/data/web_static/releases/"
                              + file_name.split(".")[0])
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(folder_to_compress))
        run("tar -xvzf /tmp/{} -C {}".format(file_name,
                                                 folder_to_compress))
        run("rm /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}/".format(folder_to_compress,
                                                 folder_to_compress))
        run("rm -rf {}/web_static".format(folder_to_compress))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_to_compress))
        return True
    except:
        return False
