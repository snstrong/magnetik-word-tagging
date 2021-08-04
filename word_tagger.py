from os import path
from typing import Set
import spacy
import csv

# Excerpt from Grimm's Fairy Tales text file used for testing
File_object = open(encoding="UTF-8", file="nightingale.txt")

nlp = spacy.load("en_core_web_sm")
doc = nlp(File_object.read())
File_object.close()

# Using a set here to eliminate duplicates
# Limitation: can only use hashable data types, so will add text or lemma and pos as tuple
wordSet = set()

for token in doc:
    if token.pos_ in ["NOUN", "VERB"]:
        wordSet.add((token.lemma_, token.pos_))
    elif token.pos_ not in ["SYM", "NUM", "PROPN", "PUNCT", "SPACE"]:
        wordSet.add((token.text, token.pos_))
        wordSet.add((token.lemma_, token.pos_))
# print(wordSet)

# Checking for expected result
if ('nightingale', 'NOUN') in wordSet:
    print(True)
else:
    print(False)

wordList = [[entry[0].lower(), entry[1]] for entry in wordSet]

print(wordList[0:10])

fields = ["word", "pos"]
rows = wordList

filename = "magnetik_word_data.csv"

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)  
    csvwriter.writerow(fields) 
    csvwriter.writerows(rows)

csvfile.close()


