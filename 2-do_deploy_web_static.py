#!/usr/bin/python3
"""
Fabric script, building upon the 1-pack_web_static.py file, to distribute an
archive to web servers.
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['35.174.205.23', '52.91.178.16']


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
    except:
        return False
