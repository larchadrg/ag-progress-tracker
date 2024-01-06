import sqlite3

def create_database(): 
    connection = sqlite3.connect('database.db')

    c = connection.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS characters (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                model TEXT,
                rank TEXT,
                genzone TEXT,
                element TEXT,
                image TEXT
                )""") 

    connection.commit()
    connection.close()
    return 

if __name__ == "__main__":
    create_database()
