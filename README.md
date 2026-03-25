# Ankify
Ankify uses 3 scripts in order to :
1. Turn your anki deck into a list of lemmas
2. Turn a whole book into a list of lemmas & their occurence number
3. Compare those two lists to get the lemmas which are in the book but not the deck, and turn them into anki cards.

## 1. DeckParser.py
The deck is imported as a CSV file. In order to obtain that CSV file, one must export the deck in anki as a .txt file, then import it into a spreadsheet software and use tabs as the separator. You can then export the spreadsheet as a CSV. The first column will be the one used, so move the words in the language you are studying to the first column.
This script supports preprocessing in order to remove superfluous material in the cards such as grammar indications.
Preprocessing is done using regex expressions.
This script outputs a list of lemmas as a .txt file with one lemma per line, which is very easy to handle for further manipulation.
