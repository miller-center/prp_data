import json
from drupal.node import Node
from drupal.nodes import Nodes
from text.idf import Idf


nodes = Nodes()
nodes.read_json()

idf = Idf()

for node in nodes.nodes:
    idf.add_documents(node.text)

print("IDF N: " + str(idf.n))

