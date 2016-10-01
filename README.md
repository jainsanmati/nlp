# nlp
Write a python program. (From a text file)
    1. To identify Named Entities using Stanford NER (Named-entity recognition)
    2. To identify ROS tags using Stanford POS Tagger
    3. To identify dependency relation using Stanford Parser

# Most of the help were taken from the site 
    http://textminingonline.com/dive-into-nltk-part-v-using-stanford-text-analysis-tools-in-python

# SYPDER-3 and Python 3.1 is used for IDE, all python code will work on that
# Steps followed and few modification 
1. Initialized the JAVAHOME veriable 
    by updating the JRE in lappy
    some times you may need to initialize java variable manualy 
    refer this: https://confluence.atlassian.com/doc/setting-the-java_home-variable-in-windows-8895.html
2. Checked that nltk package is there in system 
    if not install we can install it in windows here using command in cmd  "pip install nltk"
    then I have verified the nltk-->tag-->stanford is there 
3. imported from nltk.tag.stanford import StanfordNERTagger
    # here is a change I have imported StanfordNERTagger instead of NERTagger #Important
    then passed the environment perameters i.e. jar files path in code
    in this code path is of my lappy you may have to change that according to your package location
    Package download links are avalivale in above given link (help)
    then run the code with test statment
4. from nltk.tag.stanford import StanfordPOSTagger
    # here is a change I have imported StanfordPOSTagger instead of POSTagger #Important
    then passed the environment perameters i.e. jar files path in code
    in this code path is of my lappy you may have to change that according to your package location
    Package download links are avalivale in above given link (help)
    then run the code with test statment
5. from nltk.parse.stanford import StanfordParse
    # here I have not changed anything
    then passed the environment perameters i.e. jar files path in code
    in this code path is of my lappy you may have to change that according to your package location
    Package download links are avalivale in above given link (help)
    then run the code with test statment  
