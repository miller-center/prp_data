import re

class Vocabulary(object):
    SPACE_PATTERN = re.compile('\s+')
    DOWNCASE = True

    def __init__(self):
        self.vocab = set()
        
    def add_text(self, text):
        tokens = re.split(Vocabulary.SPACE_PATTERN, text.lower())
        # only add if this seems to be a proper noun
        if(len(tokens) != 2):
            return
        for token in tokens:
            self.vocab.add(token)
    
    def num_terms_in_vocab(self, text):
        text = text.replace(r'[\',\.]', ' ').lower()
        tokens = re.split(Vocabulary.SPACE_PATTERN, text)
        total = 0
        for token in tokens:
            if(token in self.vocab):
                total += 1  
        return total   

    def read_file(self, path_to_file):
        fh = open(path_to_file, 'r')
        lines = fh.readlines()
        fh.close()
        for line in lines:
            line = line.rstrip()
            if(Vocabulary.DOWNCASE):
                line = line.lower()
            self.vocab.add(line)