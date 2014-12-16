# Extraction of Hyponyms and words related to them 
# for word net
# Bugs to discuss:
# 1. Two word hyponym extraction
# 2. Case 3 and 4 of PDF
# 3. Bracket case (Working on it)


import nltk
from collections import Counter
import string
import operator
from decimal import *
import urllib
import re
import math
from bs4 import BeautifulSoup

html = urllib.urlopen('http://en.wikipedia.org/wiki/Car').read()
soup = BeautifulSoup(html)
[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
visible_text = soup.getText()
#print visible_text
#file = open("../Corpus.txt", "a")
#file.write(visible_text.encode('utf-8')+'\n')
#file.close()
visible_text.strip()
visible_text=visible_text.rstrip("\n")
sentences=nltk.sent_tokenize(visible_text)
stopwords=open("stopwords.txt","r")
stopwords= stopwords.read()
stopword_list=stopwords.split()
char_list=["!",'"',"``","#","$","$","%",'``',"''","&","'","(",")","*","+","-","/",":",";","<","=",">","?","@","[","\\","]","^","//","_","`","}","{","|","~"]
file_r = open("Relations.txt", "a")
file_h = open("Hyponyms.txt", "a")
for sentence in sentences:
    words=nltk.word_tokenize(sentence)
    length=len(words)
    print words
    for i in range(0,length):
        if words[i]=="such":
            if words[i+1]=="as": #CASE 1
                print "CASE 1"
                if words[i-1]=="," and (words[i-2] not in stopword_list) and (words[i-2] not in char_list):
                    file_h.write(words[i-2].encode('utf-8')+'\n')
                    file_r.write('\n'+words[i-2].encode('utf-8')+' => ')
                    print words[i-2]
                elif (words[i-1] not in stopword_list) and (words[i-1] not in char_list):
                    file_h.write(words[i-1].encode('utf-8')+'\n')
                    file_r.write('\n'+words[i-1].encode('utf-8')+' => ')
                    print words[i-1]
                else:
                    i+=2
                    continue
                i+=2
                while words[i]!="and" and words[i]!="or":
                    if words[i]==".":
                        break
                    if (words[i] in char_list) or (words[i] in stopword_list):
                        i=i+1
                        continue
                    file_r.write(" "+words[i].encode('utf-8'))
                    print words[i]
                    i=i+1
                if words[i]==".":
                    continue
                else:
                    print words[i+1]
                    if words[i+1] not in stopword_list:
                        file_r.write(', '+words[i+1].encode('utf-8'))
                #print words[i+1]
            elif words[i+2]=="as": #CASE 2
                print "CASE 2"
                if (words[i+1] not in stopword_list) and (words[i+1] not in char_list):
                    file_h.write(words[i+1].encode('utf-8')+'\n')
                    file_r.write('\n'+words[i+1].encode('utf-8')+' => ')
                print words[i+1]
                i+=3
                while words[i]!="and" and words[i]!="or":
                    if words[i]==".":
                        break
                    if (words[i] in char_list) or (words[i] in stopword_list):
                        i=i+1
                        continue
                    file_r.write(" "+words[i].encode('utf-8'))
                    print words[i]
                    i=i+1
                if words[i]==".":
                    continue
                else:
                    print words[i+1]
                    if (words[i+1] not in stopword_list) and (words[i+1] not in char_list):
                        file_r.write(', '+words[i+1].encode('utf-8'))
        elif words[i]=="other": 
            if words[i-1]=="or": #CASE 3
                print "CASE 3"
                p=0
                for j in range(0,i):
                    if words[j]=="," and (words[j+1]=="," or words[j+2]==","):
                        p=j
                        break
                if p!=0:
                    if (words[i+1] not in stopword_list) and (words[i+1] not in char_list):
                        file_h.write(words[i+1].encode('utf-8')+'\n')
                        file_r.write('\n'+words[i+1].encode('utf-8')+' => ')
                    print words[i+1]
                    file_r.write(" "+words[p-1].encode('utf-8'))
                    print words[p-1]
                    for x in range(p,i):
                        print words[x]
                        if (words[x] in char_list) or (words[x] in stopword_list):
                            continue
                        file_r.write(" "+words[x].encode('utf-8'))
            elif words[i-1]=="and":#CASE 4
                print "CASE 4"
                p=0
                for j in range(0,i):
                    if words[j]=="," and (words[j+1]=="," or words[j+2]==","):
                        p=j
                        break
                if p!=0:
                    if (words[i+1] not in stopword_list) and (words[i+1] not in char_list):
                        file_h.write(words[i+1].encode('utf-8')+'\n')
                        file_r.write('\n'+words[i+1].encode('utf-8')+' => ')
                    print words[i+1]
                    file_r.write(" "+words[p-1].encode('utf-8'))
                    print words[p-1]
                    for x in range(p,i):
                        if (words[x] in char_list) or (words[x] in stopword_list):
                            continue
                        print words[x]
                        file_r.write(" "+words[x].encode('utf-8'))
        elif words[i]=="including" or words[i]=="especially": #CASE 5 and 6
            print "CASE 5 and 6"
            if words[i-1]=="," and (words[i-2] not in stopword_list) and (words[i-2] not in char_list):
                file_h.write(words[i-2].encode('utf-8')+'\n')
                file_r.write('\n'+words[i-2].encode('utf-8')+' => ')
                print words[i-2]
            elif (words[i-1] not in stopword_list) and (words[i-1] not in char_list):
                file_h.write(words[i-1].encode('utf-8')+'\n')
                file_r.write('\n'+words[i-1].encode('utf-8')+' => ')
                print words[i-1]
            else:
                i+=1
                continue
            i+=1
            while words[i]!="and" and words[i]!="or":
                if words[i]==".":
                    break
                if (words[i] in char_list) or (words[i] in stopword_list):
                    i=i+1
                    continue
                print words[i]
                file_r.write(" "+words[i].encode('utf-8'))
                i=i+1
            if words[i]==".":
                continue
            else:
                print words[i+1]
                if words[i+1] not in stopword_list:
                    file_r.write(', '+words[i+1].encode('utf-8'))
file_r.close()
file_h.close()
