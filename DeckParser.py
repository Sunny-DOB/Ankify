from zipfile import ZipFile 
import os
import sqlite3


# Deck_path = input("Complete path of the anki deck : ")
Deck_path = "/home/SunnyDOB/Projects/German.colpkg" # hardcoded path to facilitate development.

try:
    with ZipFile(Deck_path, 'r') as UnzippedDeck:
        os.mkdir("./notes")
        UnzippedDeck.extractall(path="./notes/" )
    UnzippedDeck.close()
except FileNotFoundError:
    print("The file you're trying to access doesn't exist.")

# Create a connection and cursor to the sql database where the notes are stored
DatabaseConnection = sqlite3.connect("collection.anki2")
DatabaseCursor = DatabaseConnection.cursor()

# Query the database to get the fields of each note.
#query = 'SELECT fld FROM notes;'
DatabaseCursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(DatabaseCursor.fetchall())

DatabaseCursor.execute("SELECT * from notes;")
print(DatabaseCursor.fetchall())
# Close the cursor and sql database connection
DatabaseCursor.close()
if DatabaseConnection:
        DatabaseConnection.close()


os.remove("collection.anki2") # remove the sqlite database that is not needed anymore.


