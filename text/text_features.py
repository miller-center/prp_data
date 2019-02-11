import re
import sys
from text.vocabulary import Vocabulary

class Text_features(object):
    SPACE_PATTERN = re.compile('\s+')
    PUNCTUATION_PATTERN = re.compile(r'.*[,\.\?’\'";].*')
    YEAR_PATTERN = re.compile(r'.*1[789][0-9][0-9].*')
    NUM_PATTERN = re.compile(r'.*[0-9].*')

    def __init__(self):
        pass

    
    

    @staticmethod
    def length(s):
        tokens = re.split(Text_features.SPACE_PATTERN, s)
        return float(len(tokens))
    
    @staticmethod
    def min_tok_char_length(s):
        tokens = re.split(Text_features.SPACE_PATTERN, s)
        min = sys.maxsize
        for token in tokens:
            if(len(token) < min):
                min = len(token)
        return float(min)

    @staticmethod
    def max_tok_char_length(s):
        tokens = re.split(Text_features.SPACE_PATTERN, s)
        max = 0.0
        for token in tokens:
            if(len(token) > max):
                max = len(token)
        return float(max)
    
    @staticmethod
    def contains_punctuation(s):
        if(re.match(Text_features.PUNCTUATION_PATTERN, s)):
            return 1
        else:
            return 0
    
    @staticmethod
    def contains_year(s):
        if(re.match(Text_features.YEAR_PATTERN, s)):
            return 1
        else:
            return 0

    @staticmethod
    def contains_nonyear_number(s):
        tokens = re.split(Text_features.SPACE_PATTERN, s)
        for token in tokens:
            if(re.match(Text_features.NUM_PATTERN, token) and not re.match(Text_features.YEAR_PATTERN, token)):
                return 1
        return 0
    