from pathlib import PurePath
from tinydb import TinyDB

from os import path, mknod


def createConnection():
    database_path = PurePath('src', 'database', 'database.json')

    if not path.exists(database_path):
        mknod(database_path)

    database = TinyDB(database_path)
    return database


database = createConnection()
