#!/usr/bin/python3
"""Fabric script that creates a tgz archive from the contents
of the web_static folder in the AirBnB Clone repository."""
from datetime import datetime
from fabric.api import local
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Returns:
        The archive path if the archive has been correctly generated.
        None otherwise.
    """
    try:
        # Create versions directory if it doesn't exist
        if not os.path.exists("versions"):
            os.makedirs("versions")

        # Get the current date and time
        now = datetime.now()
        archive_name = "versions/web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))

        # Create the archive
        print("Creating archive: {}".format(archive_name))
        result = local("tar -cvzf {} web_static".format(archive_name))

        # Check if the archive was created successfully
        if result.succeeded and os.path.exists(archive_name):
            print("web_static packed: {} -> {} Bytes".format(archive_name, os.path.getsize(archive_name)))
            return archive_name
        else:
            return None
    except Exception as e:
        return None
