import json
#import gzip
from drupal.node import Node

class Nodes(object):
    PATH_TO_REGEXES = "./prp-drupal-data/all-prp-text.json"

    def __init__(self):
        self.nodes = list()


    def read_json(self):
        #with gzip.open(Nodes.PATH_TO_REGEXES, 'r') as fh:
        with open(Nodes.PATH_TO_REGEXES) as fh:
            json_text = fh.read()
            json_parsed = json.loads(json_text)

        for json_object in json_parsed:
            node = Node(json_object['nid'],
                json_object['title'],
                json_object['president'],
                json_object['date'],
                json_object['text'].split('\n'),
                json_object['participants'])
            self.nodes.append(node)  