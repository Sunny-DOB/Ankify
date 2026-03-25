import csv

UnprocessedNotesSet = set()
ProcessedNotesSet = set()

with open('German.csv', newline='') as csvfile:
    #fieldnames = ["Word", "Translation"]
    notes = csv.reader(csvfile)
    for note in notes:
        UnprocessedNotesSet.add(note[0])

StringsToRemove = ["der", "die", "das", "+A", "+D", "+G", ", en", ", er", ", e", ", ns", ", n", "(un-)", "/", "(", ")", "+", "-", "&nbsp"]
for note in UnprocessedNotesSet:
    for StringToRemove in StringsToRemove:
        note = note.replace(StringToRemove, "")
    note = note.replace(",", " ")
    ProcessedNotesSet.add(note)

print(ProcessedNotesSet)

