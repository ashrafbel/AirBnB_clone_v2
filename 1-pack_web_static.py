#!/usr/bin/python3
"""Here is a Fabric script that creates a tgz archive from the contents
of the web_static folder in the AirBnB Clone repository."""
from datetime import datetime
from fabric.api import *


def do_pack():
    local('sudo mkdir -p versions')
    d_t = datetime.now()
    d = d_t.strftime("%Y%m%d%H%M%S")
    archivename = "versions/web_static_{}.tgz".format(d)
    creating = local("tar -cvzf {} web_static".format(archivename))
    if creating is not None:
        return archivename
    else:
        return None
