import sqlite3
import csv 
 
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


load_characters()