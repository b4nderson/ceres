from pathlib import PurePath
from tinydb import TinyDB

database_path = PurePath('src', 'database', 'database.json')
database = TinyDB(database_path)
