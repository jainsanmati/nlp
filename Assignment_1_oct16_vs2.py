# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 14:42:29 2016
@author: Sanmati Jain
"""
#%%
#==============================================================================
# HELP Link all code is given here just few changes are required i.e. name of packages
#http://textminingonline.com/dive-into-nltk-part-v-using-stanford-text-analysis-tools-in-python
#==============================================================================
#%%
"""
Write a python program. (From a text file)
To identify Named Entities using Stanford NER (Named-entity recognition)
"""
#import nltk.tag.stanford
from nltk.tag.stanford import StanfordNERTagger
#==============================================================================
# nltk.tag.stanford.StanfordNERTagger
#==============================================================================
#This is just for a string
english_tagger = StanfordNERTagger('D:/SP_JAIN/16-NLP/class_assignment/stanford-ner-2015-12-09/classifiers/english.all.3class.distsim.crf.ser.gz', 'D:/SP_JAIN/16-NLP/class_assignment/stanford-ner-2015-12-09/stanford-ner.jar')
path = "D:/SP_JAIN/16-NLP/class_assignment/"
f1 = open(path + "Data_NLP_SPJain.txt","r")
myList = [i.split('\t')[0] for i in f1.readlines()]
#type(myList)
#print(myList)
op = english_tagger.tag(myList)

outfile = open(path + "Output_NER.txt","w")
#len(str(op))
#print(str(op))
for n in op:
    outfile.write("\n")
    for i in str(n):
        outfile.write(i)

outfile.close()
#english_tagger.tag(('Rami Eid is studying at Stony Brook University in NY'.split()))

#==============================================================================
#%%
"""
Write a python program. (From a text file)
To identify ROS tags using Stanford POS Tagger
"""
from nltk.tag.stanford import StanfordPOSTagger
english_postagger = StanfordPOSTagger('D:/SP_JAIN/16-NLP/class_assignment/stanford-postagger-full-2014-08-27/models/english-bidirectional-distsim.tagger', 'D:/SP_JAIN/16-NLP/class_assignment/stanford-postagger-full-2014-08-27/stanford-postagger.jar')

path = "D:/SP_JAIN/16-NLP/class_assignment/"
f1 = open(path + "demo.txt","r")
myList = [i.split('\t')[0] for i in f1.readlines()]
#type(myList)
#print(myList)

op = english_postagger.tag(myList)

outfile = open(path + "Output_POS.txt","w")
#len(str(op))
#print(str(op))
for n in op:
    outfile.write("\n")
    for i in str(n):
        outfile.write(i)

outfile.close()

#%%
"""
Write a python program. (From a text file)
C.	To identify dependency relation using Stanford Parser
"""
#import nltk.tag.stanford
from nltk.parse.stanford import StanfordParser

english_parser = StanfordParser('D:/SP_JAIN/16-NLP/class_assignment/stanford-parser-full-2014-08-27/stanford-parser.jar', 'D:/SP_JAIN/16-NLP/class_assignment/stanford-parser-full-2014-08-27/stanford-parser-3.4.1-models.jar')

path = "D:/SP_JAIN/16-NLP/class_assignment/"
f1 = open(path + "demo.txt","r")
myList = [i.split('\t')[0] for i in f1.readlines()]
#type(myList)
#print(myList)

#sentences = english_parser.raw_parse_sents(myList)

#==============================================================================
# for myListiterator in sentences:
#     for t in myListiterator:
#         print(t.leaves())
#==============================================================================

        
sentences = english_parser.raw_parse_sents(myList)       
outfile = open(path + "Output_Parser.txt","w")
for myListiterator in sentences:
    for t in myListiterator:
        outfile.write(str(t))
        #print(str(t.leaves()))
outfile.close()

#==============================================================================
# 
# 
#   File "<ipython-input-210-9f9cf27673a4>", line 25, in <module>
#     sentences = english_parser.raw_parse_sents(myList)
# 
#   File "C:\Program Files\Anaconda3\lib\site-packages\nltk\parse\stanford.py", line 150, in raw_parse_sents
#     return self._parse_trees_output(self._execute(cmd, '\n'.join(sentences), verbose))
# 
#   File "C:\Program Files\Anaconda3\lib\site-packages\nltk\parse\stanford.py", line 220, in _execute
#     stdout = stdout.decode(encoding)
# 
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf6 in position 53792: invalid start byte
# #%%
#==============================================================================








