import sqlite3
import csv
import os
from config import ROOT_PATH

DB_PATH = os.path.join(ROOT_PATH, "app", "instance", "database.db")
DELIMITER_CSV = ","

def load_characters():
    CHRACTERS_CSV_PATH = os.path.join(ROOT_PATH, "characters.csv")

    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(DB_PATH)
        c = connection.cursor()

        # Open and read the CSV file
        with open(CHRACTERS_CSV_PATH, 'r', encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=DELIMITER_CSV)  # Use semicolon as delimiter
            next(reader)  # Skip the header row
            
            for row in reader:
                print(f"Row data: {row}")  # Debug: Print each row's data

                if len(row) != 6:
                    print(f"Warning: Row does not have 6 columns. Skipping row: {row}")
                    continue

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

        # Commit changes and close the connection
        connection.commit()
    except FileNotFoundError:
        print(f"Error: The file {CHRACTERS_CSV_PATH} does not exist.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()

# Call the function
load_characters()
