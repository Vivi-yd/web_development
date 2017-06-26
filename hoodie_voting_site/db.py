import sqlite3
import os

data_path = os.path.dirname(os.path.realpath(__file__))
dbname = "dataset.db"

try:
    os.mkdir(data_path)
except OSError:
    pass

db_path = os.path.join(data_path, dbname)
db = sqlite3.connect(db_path)
db.execute("PRAGMA foreign_keys = 1")
