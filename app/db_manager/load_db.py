import sqlite3
import csv
from .csv_paths import *
from .insert_queries import * 
from os.path import dirname, abspath, join

BASE_DIR = dirname(abspath(__file__))
DB_PATH = join(BASE_DIR, "..", "instance",'database.db')
SCHEMA_PATH = join(BASE_DIR,'schema.sql')

def load_db_data(path, delimiter, columns, query, skip_head=True):
    try:
        connection = sqlite3.connect(DB_PATH)
        c = connection.cursor()
        with open(path, 'r', encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=delimiter)  # Use semicolon as delimiter
            if skip_head: 
                next(reader)  # Skip the header row
            
            for row in reader:

                if len(row) != columns:
                    print(f"Warning: Row does not have {columns} columns. Skipping row: {row}")
                    continue

                c.execute(query, row)

                connection.commit()
    except FileNotFoundError:
        print(f"Error: The file {path} does not exist.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()

def load_ag_data(): 
    load_db_data(CHARACTERS_CSV_PATH, ",", 7, CHARACTERS_QUERY, True)
    load_db_data(ELEMENTS_CSV_PATH, '|', 3, ELEMENTS_QUERY, False) 
    load_db_data(RANKS_CSV_PATH, '|', 2, RANKS_QUERY, False) 
    load_db_data(SIGILS_CSV_PATH, '|',3,SIGILS_QUERY, False) 
    load_db_data(WARP_SKILLS_CSV_PATH,'|',5, WARP_SKILLS_QUERY, False)
    load_db_data(FUNCTORS_CSV_PATH, ';', 6, FUNCTORS_QUERY, True)
if __name__ == '__main__': 
    load_ag_data()