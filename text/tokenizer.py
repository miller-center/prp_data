import string
import re

class Tokenizer(object):
    translator = str.maketrans('', '', string.punctuation)
    space_regex = re.compile('\s+')

    def __init__(self):
        pass

    @staticmethod
    def tokenize(s):
        # remove punctuation
        s = s.translate(Tokenizer.translator)
        # downcase
        s = s.lower()
        # trim whitespace
        s = s.strip()
        # groom whitespace for splitting
        s = re.sub(Tokenizer.space_regex, " ", s)
        # and finally, do the split
        return s.split()

