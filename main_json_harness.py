import json
from drupal.node import Node
from drupal.nodes import Nodes



nodes = Nodes()
nodes.read_json()

for node in nodes.nodes:
    print(node.nid + '\t' + str(len(node.text)))
