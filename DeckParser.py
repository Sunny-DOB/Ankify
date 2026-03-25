import csv

NotesSet = set()

with open('German.csv', newline='') as csvfile:
    #fieldnames = ["Word", "Translation"]
    notes = csv.reader(csvfile)
    for note in notes:
        NotesSet.add(note[0])

csvfile.close()
print(NotesSet)

