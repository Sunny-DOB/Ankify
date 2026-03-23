from zipfile import ZipFile 
import os


# Deck_path = input("Complete path of the anki deck : ")
Deck_path = "/home/SunnyDOB/Projects/Ankify/GermanVoc.apkg" # hardcoded path to facilitate development.

try:
    with ZipFile(Deck_path, 'r') as UnzippedDeck:
        UnzippedDeck.extract("collection.anki2", path="./")
    UnzippedDeck.close()
except FileNotFoundError:
    print("The file you're trying to access doesn't exist.")

os.remove("collection.anki2") # remove the sqlite database that is not needed anymore.


