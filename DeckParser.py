import csv

with open('German.csv', newline='') as csvfile:
    fieldnames = ["Word", "Translation"]
    notes = csv.DictReader(csvfile, fieldnames=fieldnames)
    for note in notes:
        print(note["Word"])

