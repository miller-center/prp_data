"""
    Takes two files as input:
        tags/regexes: a set of n tags with one or more regexes per tag specified
        node json: a big dump of json-encoded drupal nodes (for PRP docs)

    The program steps over each node and applies all tags that have at least one
    regex that matches the textual content of the node/metadata.  The matches/tags 
    are serialized as a new json object, a list of node_id => (list, of tags).
"""

import json
import re
from drupal.node import Node
from drupal.nodes import Nodes

tags_regex = {}
path_to_regexes = "./prp-drupal-data/config-taxonomy-terms-regexes.txt"
fh = open(path_to_regexes, 'r')
r_lines = fh.readlines()
fh.close()
for r_line in r_lines:
    (tag_name,regex_string) = r_line.rstrip().split(':')
    regexes = regex_string.split(',')
    for regex in regexes:
        regex = '.*\W' + regex + '\W.*'
        pattern = re.compile(regex)
        tags_regex[pattern] = tag_name



nodes = Nodes()
nodes.read_json()

node_tags = {}

for node in nodes.nodes:
    if(node.nid not in node_tags):
        node_tags[node.nid] = set()
    tags_for_node = node_tags[node.nid]
    node_text = node.get_all_text().lower()
    for pattern in tags_regex:
        if(pattern.match(node_text)):
            #print(node.nid + '\t\t' + tags_regex[pattern])
            node_tags[node.nid].add(tags_regex[pattern])

# convert sets to lists for JSON serialization...dumb!
for node_id in node_tags:
    tags = list(node_tags[node_id])
    node_tags[node_id] = tags

print(json.dumps(node_tags))
