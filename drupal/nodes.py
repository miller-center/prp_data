import json
from drupal.node import Node

class Nodes(object):

    def __init__(self):
        self.nodes = list()


    def read_json(self, path_to_json):
        with open(path_to_json) as fh:
            json_text = fh.read()
            json_parsed = json.loads(json_text)

        for json_object in json_parsed:
            node = Node(json_object['nid'],
                json_object['president'],
                json_object['date'],
                json_object['text'],
                json_object['participants'])
            self.nodes.append(node)  