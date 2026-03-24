import csv

with open('German.csv', newline='') as csvfile:
    #fieldnames = ["Word", "Translation"]
    notes = csv.reader(csvfile)
    for note in notes:
        print(note[0])

