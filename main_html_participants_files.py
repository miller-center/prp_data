"""
    Generates a bunch of small HTML files: one file per "participant" from the
    PRP tapes.
"""

import json
import sys
import operator
from drupal.node import Node
from drupal.nodes import Nodes





person_dir = "person_files"

nodes = Nodes()
nodes.read_json()

# name -> (list, of, html, strings)
name_pointers = {}

# initialize our array of name->html lists
for node in nodes.nodes:
    node_pres = node.president
    node_participants = node.participants
    nid = node.nid
    date = node.date
    president = node.president
    title = node.title
    url = 'https://millercenter.org/node/' + nid
    recording_title = date + ': ' + title
    text_entry = '<li><a href="' + url + '">' + recording_title + '</a>. (' + president + ')' + '</li>\n'
    key = recording_title + '::' + text_entry
    for participant in node_participants:
        if(participant not in name_pointers):
            name_pointers[participant] = list()
        name_pointers[participant].append(key)
        
for name in name_pointers:
    print(name + ":: " + str(len(name_pointers[name])))
    file_name = person_dir + "/" + name.replace(' ', '_') + ".html"
    of = open(file_name, mode='w')

    of.write('<html>\n')
    of.write('<link rel="stylesheet" href="../style.css"/>\n')
    of.write('<title>' + name + '</title>\n')
    of.write('<body>\n')
    of.write('<h1>' + name + '</name></h1>\n')
    of.write('<ol>\n')

    entries = name_pointers[name]
    entries.sort()

    for entry in entries:
        # the 'dummy' field is the key we defined earlier to induce a proper sort.
        (dummy, entry) = entry.split('::')
        of.write(entry + '\n')

    of.write('</ol>\n')
    of.write('</body>\n')
    of.write('</html>\n')
