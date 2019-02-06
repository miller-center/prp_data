"""
A class that stores data and handles basic operations related
to TF-IDF weighting in the context of a particular corpus.
"""

from text.tokenizer import Tokenizer
from math import log

class Idf(object):

    def __init__(self):
        self.n = 0
        self.vocabulary = {} # term -> doc_freq pairs
    
    def idf(self, term):
        if term not in self.vocabulary:
            return 0
        else:
            return log(self.n / self.vocabulary[term])


    def add_token(self, token):
        if(token not in self.vocabulary):
            self.vocabulary[token] = 1
        else:
            self.vocabulary[token] += 1
    
    def add_document(self, text):
        if(text == '\n'):
            return
        self.n += 1
        tokens = Tokenizer.tokenize(text)
        for token in tokens:
            self.add_token(token)
    
    def add_documents(self, texts):
        for text in texts:
            self.add_document(text)

    