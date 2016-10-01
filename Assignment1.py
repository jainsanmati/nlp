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

#%%
"""
Write a python program. (From a text file)
To identify ROS tags using Stanford POS Tagger
"""
#import nltk.tag.stanford
from nltk.parse.stanford import StanfordParser

english_parser = StanfordParser('D:/SP_JAIN/16-NLP/class_assignment/stanford-postagger-full-2014-08-27/stanford-parser.jar', 'stanford-parser-3.4-modelsstanford-postagger-3.4.1.jar')
