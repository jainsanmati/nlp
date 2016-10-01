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
demo = StanfordNERTagger('D:/SP_JAIN/16-NLP/class_assignment/stanford-ner-2015-12-09/classifiers/english.all.3class.distsim.crf.ser.gz', 'D:/SP_JAIN/16-NLP/class_assignment/stanford-ner-2015-12-09/stanford-ner.jar')
demo.tag(('Rami Eid is studying at Stony Brook University in NY'.split()))

#==============================================================================
# OUTPUT
# Out[39]: 
# [('Rami', 'PERSON'),
#  ('Eid', 'PERSON'),
#  ('is', 'O'),
#  ('studying', 'O'),
#  ('at', 'O'),
#  ('Stony', 'ORGANIZATION'),
#  ('Brook', 'ORGANIZATION'),
#  ('University', 'ORGANIZATION'),
#  ('in', 'O'),
#  ('NY', 'O')]
#==============================================================================
#%%
"""
Write a python program. (From a text file)
To identify ROS tags using Stanford POS Tagger
"""
from nltk.tag.stanford import StanfordPOSTagger
english_postagger = StanfordPOSTagger('D:/SP_JAIN/16-NLP/class_assignment/stanford-postagger-full-2014-08-27/models/english-bidirectional-distsim.tagger', 'D:/SP_JAIN/16-NLP/class_assignment/stanford-postagger-full-2014-08-27/stanford-postagger.jar')
english_postagger.tag('this is stanford postagger in nltk for python users'.split())

#==============================================================================
# #OUTPUT
# Out[45]: 
# [('this', 'DT'),
#  ('is', 'VBZ'),
#  ('stanford', 'JJ'),
#  ('postagger', 'NN'),
#  ('in', 'IN'),
#  ('nltk', 'NN'),
#  ('for', 'IN'),
#  ('python', 'NN'),
#  ('users', 'NNS')]
# 
#==============================================================================

#%%
"""
Write a python program. (From a text file)
C.	To identify dependency relation using Stanford Parser
"""
#import nltk.tag.stanford
from nltk.parse.stanford import StanfordParser
from nltk import*

english_parser = StanfordParser('D:/SP_JAIN/16-NLP/class_assignment/stanford-parser-full-2014-08-27/stanford-parser.jar', 'D:/SP_JAIN/16-NLP/class_assignment/stanford-parser-full-2014-08-27/stanford-parser-3.4.1-models.jar')
sentences = english_parser.raw_parse_sents(('this is the english parser test', 'the parser is from stanford parser'))

for myListiterator in sentences:
    for t in myListiterator:
        print(t)
        
#==============================================================================
# #OUTPUT
# (ROOT
#   (S
#     (NP (DT this))
#     (VP (VBZ is) (NP (DT the) (JJ english) (NN parser) (NN test)))))
# (ROOT
#   (S
#     (NP (DT the) (NN parser))
#     (VP (VBZ is) (PP (IN from) (NP (JJ stanford) (NN parser))))))
#==============================================================================

#%%
