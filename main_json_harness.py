import json
from drupal.node import Node
from drupal.nodes import Nodes


path_to_json = "/Users/mefron/prp/data/all-prp-text.json"

nodes = Nodes()
nodes.read_json(path_to_json)

for node in nodes.nodes:
    print(node.nid + '\t' + node.president)
