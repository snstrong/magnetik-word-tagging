from os import path
from typing import Set
import spacy
import csv

File_object = open(encoding="UTF-8", file="grimms-fairy-tales.txt")

# Using SpaCy's tagging features to get parts of speech for each word in file
nlp = spacy.load("en_core_web_sm")
doc = nlp(File_object.read())

File_object.close()

# Using a set here to eliminate duplicates
# Set can only use hashable data types, so will add text/lemma and part of speech(pos) as tuple
wordSet = set()

for token in doc:
    if token.pos_ in ["NOUN", "VERB"]:
        # Only using lemmas here to get the "pure" form of the noun or verb (i.e., without pluralization or conjugation)
        wordSet.add((token.lemma_.lower(), token.pos_))
    elif token.pos_ not in ["SYM", "NUM", "PROPN", "PUNCT", "SPACE"]:
        # Not adding symbols, numbers, proper nouns, punctuation, or spaces. Will need to add punctuation later, but was concerned about causing issues with csv file
        wordSet.add((token.text.lower(), token.pos_))
        wordSet.add((token.lemma_.lower(), token.pos_))

# Writing to csv
fields = ["word", "pos"]
rows = [[entry[0], entry[1]] for entry in wordSet]

filename = "magnetik_word_data.csv"

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)  
    csvwriter.writerow(fields) 
    csvwriter.writerows(rows)

csvfile.close()


