"""
    Generates a 2-column table, one row per participant name, with Column
    1 = that person's overall frequency of appearance as a participant
    in the corpus.

    optional parameter: specify a president (in [DDE, FDR, JDF, LBJ, 
    RMN], in which case, counts are limited to just that administration).
"""

import json
import sys
from drupal.node import Node
from drupal.nodes import Nodes

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



path_to_json = "/Users/mefron/prp/data/all-prp-text.json"

nodes = Nodes()
nodes.read_json(path_to_json)

counts = {}

for node in nodes.nodes:
    node_pres = node.president
    filter = True
    if(limiter and limiter != node_pres):
        filter = False
    
    if(filter):
        node_participants = node.participants
        for participant in node_participants:
            if(participant not in counts):
                counts[participant] = 1
            else:
                counts[participant] += 1

for participant in counts:
    print(f'{counts[participant]}\t\t{participant}')