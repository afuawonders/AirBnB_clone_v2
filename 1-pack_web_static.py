#!/usr/bin/python3
# Fabfile to generate a .tgz archive from the contents of web_static.
import os
import subprocess
from datetime import datetime

def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

    if not os.path.exists("versions"):
        subprocess.run(["mkdir", "-p", "versions"])

    result = subprocess.run(["tar", "-cvzf", file, "web_static"])

    if result.returncode != 0:
        return None

    return file
