"""
    Generates a 2-column table, one row per participant name, with Column
    1 = that person's overall frequency of appearance as a participant
    in the corpus.

    optional parameter: specify a president (in [DDE, FDR, JDF, LBJ, 
    RMN], in which case, counts are limited to just that administration).
"""

import json
import sys
import operator
import re
from drupal.node import Node
from drupal.nodes import Nodes
from text.idf import Idf

order_by = "idf"

limiter = ""
if(len(sys.argv)==2):
    pr = sys.argv[1].lower()
    if(pr == 'dde'):
        limiter = 'Dwight D. Eisenhower'
    elif(pr == 'fdr'):
        limiter = 'Franklin D. Roosevelt'
    elif(pr == 'jfk'):
        limiter = 'John F. Kennedy'
    elif(pr == 'lbj'):
        limiter = 'Lyndon B. Johnson'
    elif(pr == 'rmn'):
        limiter = "Richard Nixon"
    else:
        print('Illegal president/limiter: ' + sys.argv[1])
        exit(1)



nodes = Nodes()
nodes.read_json()

counts = {}

idf = Idf()

for node in nodes.nodes:
    node_pres = node.president
    filter = True
    if(limiter and limiter != node_pres):
        filter = False
    
    if(filter):
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
if(order_by == 'idf'):
    for term in counts:
        term_count = counts[term]
        term_idf   = idf.idf_ngram_min(term)
        tf_idf[term] = term_idf * term_count
    sorted_d = sorted(tf_idf.items(), key=operator.itemgetter(1), reverse=True)


for k, v in sorted_d:
    print(f'{v}\t\t{k}')
