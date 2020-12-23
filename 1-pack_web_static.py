#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from
the contents of the web_static
"""
from time import strftime
from datetime import date
from fabric.api import local


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
