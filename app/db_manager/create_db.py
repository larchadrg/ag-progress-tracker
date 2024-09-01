import sqlite3
from os.path import join, abspath, dirname 
BASE_DIR = dirname(abspath(__file__))
DB_PATH = join(BASE_DIR, "..", "instance",'database.db')
SCHEMA_PATH = join(BASE_DIR,'schema.sql')

def create_database(): 

    with open(SCHEMA_PATH, 'r') as sql_file:
        sql_script = sql_file.read()

    try:
        connection = sqlite3.connect(DB_PATH)
        c = connection.cursor()
        c.executescript(sql_script)
        connection.commit()

    except sqlite3.DatabaseError as e: 
            print(f"Cant open schema file: {DB_PATH}")
          
    except sqlite3.Error as e:
            print(f"Database error: {e}")
    finally:
            connection.close()


if __name__ == "__main__": 
      create_database()