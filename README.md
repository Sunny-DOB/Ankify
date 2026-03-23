# Ankify
Ankify uses 3 scripts in order to :
1. Turn your anki deck into a list of lemmas
2. Turn a whole book into a list of lemmas & their occurence number
3. Compare those two lists to get the lemmas which are in the book but not the deck, and turn them into anki cards.

## 1. DeckParser.py
This script supports preprocessing in order to remove superfluous material in the cards such as grammar indications.
Preprocessing is done using regex expressions.
This script outputs a list of lemmas as a 
