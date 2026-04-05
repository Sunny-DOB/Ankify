import spacy

KnownLemmas = set()
UnknownLemmas = set()
KnownNotes = set()
BookLemmas = {}
UnknownLemmas = set()
OccurencesThreshold = 2 # minimum number of times

with open("ProcessedNotes.txt", "r") as ProcessedNotes:
    for Note in ProcessedNotes:
        KnownNotes.add(Note.strip())
        
nlp = spacy.load("de_core_news_lg") # de_dep_news_trf displays superior performance at a reduced size, but doesn't work in nix-shell. Switching to the transformer model would be best.
lemmatizer = nlp.get_pipe("lemmatizer")

for Note in KnownNotes:
    RawNote = nlp(Note)
    for token in RawNote:
        if token.text is not token.is_stop: #Check the token is not a stop word
            KnownLemmas.add(token.lemma_) 

Book = "Schachnovelle.txt"
with open(Book, "r") as BookFile:
    BookContents = nlp(BookFile.read())

for token in BookContents:
    if token.text is not token.is_stop:
        if token.lemma_ in BookLemmas:
            BookLemmas[token.lemma_] += 1
        else:
            BookLemmas[token.lemma_] = 1

for BookLemma in BookLemmas:
    if BookLemma not in KnownLemmas:
        if BookLemmas[BookLemma] >= OccurencesThreshold:
            UnknownLemmas.add(BookLemma)
        

print(len(UnknownLemmas))
