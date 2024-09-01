import sqlite3
from os.path import join, abspath

DB_PATH = abspath(join("instance",'database.db'))
SCHEMA_PATH = abspath(join('db_manager', 'schema.sql'))

def create_database(): 

    with open(SCHEMA_PATH, 'r') as sql_file:
        sql_script = sql_file.read()

    try:
        connection = sqlite3.connect(DB_PATH)
        c = connection.cursor()
        c.executescript(sql_script)
        connection.commit()
    except sqlite3.Error as e:
            print(f"Database error: {e}")
    finally:
            connection.close()


if __name__ == "__main__": 
      create_database()