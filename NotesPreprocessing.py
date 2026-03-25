import csv

UnprocessedNotesSet = set()
ProcessedNotesSet = set()

with open('German.csv', newline='') as csvfile:
    #fieldnames = ["Word", "Translation"]
    notes = csv.reader(csvfile)
    for note in notes:
        UnprocessedNotesSet.add(note[0])

StringsToRemove = ["der ", "die ", "das ", "+A", "+D", "+G", ", en", ", er", ", e", ", ns", ", n", ", ses", ", se", ", es", "-in", ", s", ", i", ", a", ", ei", ", ie", " A ", " D ", "<br>", ";", "(un-)", "(", ")", "+", "-", "&nbsp", "<b>", "qn", "qc", "="] 
for note in UnprocessedNotesSet:
    for UnwantedSubstring in StringsToRemove:
        note = note.replace(UnwantedSubstring, "")
    note = note.replace(",", " ")
    note = note.replace("/", " ")
    note = note.replace("\n", " ")
    ProcessedNotesSet.add(note)

with open("ProcessedNotes.txt", "w") as ProcessedNotesFiles:
    for note in ProcessedNotesSet:
        ProcessedNotesFiles.write(note + "\n")



print(ProcessedNotesSet)

