from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Returns:
        The archive path if the archive has been correctly generated.
        None otherwise.
    """
    # Create versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Create the archive name
    now = datetime.now()
    archive_name = "versions/web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))

    # Create the archive
    try:
        print("Packing web_static to {}".format(archive_name))
        local("tar -cvzf {} web_static".format(archive_name))
        print("web_static packed: {} -> {}Bytes".format(archive_name, os.path.getsize(archive_name)))
        return archive_name
    except Exception as e:
        print("An error occurred: {}".format(e))
        return None
