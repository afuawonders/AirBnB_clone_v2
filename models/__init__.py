#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from os import getenv


#!/usr/bin/python3
"""Defines the storage engine for the application."""

# Check the value of the HBNB_TYPE_STORAGE environment variable
if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()



storage = FileStorage()
storage.reload()
