"""
    Generates a CSV file for assesing the merits (based on column-wise features)
    of a sample of candidate 'keywords.'
"""

import json
import sys
import operator
import re
from drupal.node import Node
from drupal.nodes import Nodes
from text.idf import Idf
from text.text_features import Text_features
from text.vocabulary import Vocabulary

order_by_idf = True


nodes = Nodes()
nodes.read_json()

counts = {}
idf = Idf()
proper_names = Vocabulary()
place_names  = Vocabulary()
place_names.read_file("prp-drupal-data/place_names.txt")


for node in nodes.nodes:
    node_pres = node.president
    
    participants = node.participants
    for participant in participants:
        proper_names.add_text(participant)

    node_text_lines = node.text
    for line in node_text_lines:
        line = re.sub('^\s+', '', line).lower()
        line = re.sub('^-', '', line)
        if(len(line) > 1):
            idf.add_document(line)
            if(line not in counts):
                counts[line] = 1
            else:
                counts[line] += 1



sorted_d = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)

tf_idf = {}
if(order_by_idf == True):
    for term in counts:
        term_count = counts[term]
        term_idf   = idf.idf_ngram_min(term)
        tf_idf[term] = term_idf * term_count
    sorted_d = sorted(tf_idf.items(), key=operator.itemgetter(1), reverse=True)


print(
    'is_valid ' +
    'frequency ' +
    'tf_idf ' +
    'length ' +
    'min_char_len ' +
    'max_char_len ' +
    'proper_names ' +
    'place_names ' +
    'punctuation ' +
    'year ' +
    'numbers'
)
for term, idf in sorted_d:
    print(
        str(0) + ' ' +
        str(counts[term]) + ' ' +
        str(idf) + ' ' +
        str(Text_features.length(term)) + ' ' +
        str(Text_features.min_tok_char_length(term)) + ' ' + 
        str(Text_features.max_tok_char_length(term)) + ' ' +
        str(proper_names.num_terms_in_vocab(term)) + ' ' + 
        str(place_names.num_terms_in_vocab(term)) + ' ' + 
        str(Text_features.contains_punctuation(term)) + ' ' + 
        str(Text_features.contains_year(term)) + ' ' +
        str(Text_features.contains_nonyear_number(term)) + 
        '\t\t# ' + term
    )
