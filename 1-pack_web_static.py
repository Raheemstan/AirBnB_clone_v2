def do_pack():
    """
    Create a .tgz archive from the contents of the web_static folder
    """

    from datetime import datetime
    from fabric.api import local
    import os

    # Create the versions folder if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Generate the archive name
    time = datetime.now()
    archive_name = "web_static_" + time.strftime("%Y%m%d%H%M%S") + ".tgz"

    # Create the archive
    result = local("tar -cvzf versions/{} web_static".format(archive_name))

    # Return the archive path if the archive has been correctly generated
    if result.succeeded:
        return "versions/{}".format(archive_name)
    else:
        return None
