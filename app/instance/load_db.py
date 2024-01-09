import sqlite3
import csv 

DB_PATH = r"C:\Users\larac\Documents\ag-progress-tracker\app\instance\database.db"
SIGIL_CSV_PATH = r"C:\Users\larac\Documents\ag-progress-tracker\scraping\data\sigils.csv" 

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
            c.execute("INSERT INTO sigils (name, image) VALUES (?, ?)", row)
        connection.commit()
    connection.close()
    return

load_sigils()