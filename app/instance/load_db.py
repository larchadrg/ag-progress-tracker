import sqlite3
import csv 
from warp_effects import data_to_insert

DB_PATH = r"C:\Users\larac\Documents\ag-progress-tracker\app\instance\database.db"
SIGIL_CSV_PATH = r"C:\Users\larac\Documents\ag-progress-tracker\scraping\data\sigils_fixed.csv" 

def load_characters(): 

    connection = sqlite3.connect('database.db')
    c = connection.cursor()
    with open('characters.csv', 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        reader.__next__()
        for row in reader:
            c.execute("INSERT INTO characters (name, model, rank, genzone, element, image) VALUES (?, ?, ?, ?, ?, ?)", row)
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

load_warp_effects()