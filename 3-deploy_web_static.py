#!/usr/bin/python3
"""
Fabric script, building upon the 1-pack_web_static.py file, to distribute an
archive to web servers.
"""

from fabric.api import put, run, env
from os.path import exists
from datetime import datetime
from fabric.api import *


env.hosts = ['35.174.205.23', '52.91.178.16']


def do_pack():
    "tgz archive genereted"
    local('sudo mkdir -p versions')
    d_t = datetime.now()
    d = d_t.strftime("%Y%m%d%H%M%S")
    archivename = "versions/web_static_{}.tgz".format(d)
    creating = local("tar -cvzf {} web_static".format(archivename))
    if creating is not None:
        return archivename
    else:
        return None


def do_deploy(archive_path):
    """deploys an archive to web servers"""
    if exists(archive_path) is False:
        return False
    try:
        f_n = archive_path.split("/")[-1]
        basename = f_n.split(".")[0]
        p = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(p, basename))
        run('tar -xzf /tmp/{} -C {}{}/'.format(f_n, p, basename))
        run('rm /tmp/{}'.format(f_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(p, basename))
        run('rm -rf {}{}/web_static'.format(p, basename))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(p, basename))
        return True
    except Exception:
        return False


def deploy():
    """Creates and deploys an archive to web servers."""
    narchivepath = do_pack()
    if exists(narchivepath) is False:
        return False
    result = do_deploy(narchivepath)
    return result
