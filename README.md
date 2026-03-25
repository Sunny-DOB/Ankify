# Ankify
Ankify is composed of several scripts, whose roles are explained in this document. The first script's role is to preprocess the notes to improve the precision of the tokenization and lemmatization steps.
The second script's role is to tokenize and lemmatize the list of notes that was created using the first script, and the text of the book (using spacy), and create a csv with all the lemmas that haven't been learned yet, and the number of times they appear in the text.
The third scripts role is to take the lemmas that are outputted by the second script and turn them into anki cards in an anki deck.

## 1. NotesPreprocessing.py
The deck is imported as a CSV file. In order to obtain that CSV file, one must export the deck in anki as a .txt file, then import it into a spreadsheet software and use tabs as the separator. You can then export the spreadsheet as a CSV. The first column will be the one used, so move the words in the language you are studying to the first column.
This script supports preprocessing in order to remove superfluous material in the cards such as grammar indications.
Preprocessing is done using a hardcoded list of substrings to remove.
This script outputs a list of lemmas as a .txt file with one lemma per line, which is very easy to handle for further manipulation.
