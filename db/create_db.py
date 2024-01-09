import sqlite3

def create_database():
    db_path = r"C:\Users\larac\Documents\ag-progress-tracker\app\instance\database.db" 
    connection = sqlite3.connect(db_path)

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
    
    c.execute("""CREATE TABLE IF NOT EXISTS sigils (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                image TEXT NOT NULL
                )""") 

    connection.commit()
    connection.close()
    return 

if __name__ == "__main__":
    create_database()
