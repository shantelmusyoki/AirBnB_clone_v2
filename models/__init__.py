#!/usr/bin/python3
"""This module instantiates an object of class FileStorage

If the environment variable 'HBNB_TYPE_STORAGE' is set to 'db',
instatiate a database storage engine (DBStorage)

Otherwise, instatiate a filestorage engine
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
