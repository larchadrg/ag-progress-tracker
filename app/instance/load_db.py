import sqlite3
import csv 
import os 

ROOT_PATH = r"/home/lara-uni/Documents/ag-progress-tracker" 
DB_PATH = os.path.join(ROOT_PATH, "app", "instance", "database.db")

def load_characters(): 
    CHRACTERS_CSV_PATH = os.path.join(ROOT_PATH, "characters.csv")

    connection = sqlite3.connect(DB_PATH)
    c = connection.cursor()
    with open(CHRACTERS_CSV_PATH, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        reader.__next__() #ignore headers 
        for row in reader:
            c.execute("""
            INSERT INTO characters (id, name, model, rank, genzone, image)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    name = excluded.name,
                    model = excluded.model,
                    rank = excluded.rank,
                    genzone = excluded.genzone,
                    image = excluded.image
            """, row)
        connection.commit()
    connection.close()
    return

def load_sigils():
    connection = sqlite3.connect(DB_PATH)
    c = connection.cursor()
    with open(SIGIL_CSV_PATH, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        reader.__next__()
        for row in reader:
            c.execute("INSERT INTO sigils (name, image) VALUES (?, ?)", row[1:])
        connection.commit()
    connection.close()
    return

def load_warp_effects():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.executemany('INSERT INTO warp_skills (name, image, slot1, slot2) VALUES (?, ?, ?, ?)', data_to_insert)
    connection.commit()
    connection.close()
    return

load_characters()