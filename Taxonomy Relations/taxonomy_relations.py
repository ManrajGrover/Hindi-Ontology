import nltk
from collections import Counter
import string
import operator
from decimal import *
import urllib
import re
import math
from bs4 import BeautifulSoup

html = urllib.urlopen('http://en.wikipedia.org/wiki/Color').read()
soup = BeautifulSoup(html)
[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
visible_text = soup.getText()
print visible_text
file = open("Corpus.txt", "a")
file.write(visible_text.encode('utf-8')+'\n')
file.close()
visible_text.strip()
visible_text=visible_text.rstrip("\n")
sentences=nltk.sent_tokenize(visible_text)
file = open("Extracted Relations.txt", "a")
for sentence in sentences:
    words=nltk.word_tokenize(sentence)
    length=len(words)
    for i in range(0,length):
        if words[i]=='of':
            if words[i+1]=='the':
                print words[i-1]+" => "+words[i+2] #Attribute Concept
                file.write(words[i+2].encode('utf-8')+" => "+words[i-1].encode('utf-8')+'\n')
        elif words[i]=='is':
            if words[i+1]=='a':
                print words[i-1]+" => "+words[i+2] #Value Attribute
                file.write(words[i+2].encode('utf-8')+" => "+words[i-1].encode('utf-8')+'\n')
        elif words[i]=='the':
            if i+4>=length:
                break
            elif words[i+4]=='is':
                print words[i+1]+" => "+words[i+2] #Value Concept
                file.write(words[i+2].encode('utf-8')+" => "+words[i+1].encode('utf-8')+'\n')
file.close()
