"""
    Generates an HTML menu-page: one entry per "participant" from the
    PRP tapes.
"""

import json
import sys
import operator
from drupal.node import Node
from drupal.nodes import Nodes







nodes = Nodes()
nodes.read_json()

counts = {}

for node in nodes.nodes:
    node_pres = node.president
    node_participants = node.participants
    for participant in node_participants:
        if(participant not in counts):
            counts[participant] = 1
        else:
            counts[participant] += 1



# HTML frontmatter
print('<html>\n')
print('<head>\n')
print('<title>PRP Participants</title>\n')
print('<link rel="stylesheet" href="style.css"/>\n')
print('<body>\n')
print('<table>\n')

sorted_d = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)
for name, count in sorted_d:
    name = name.replace(' ', '_')
    link_file = "person_files/" + name + ".html"
    print('<tr>\n')
    print('<td>' + str(count) + '</td><td>' +
            '<a href="./' + link_file + '">' + name + '</a></td>\n')
    print('</tr>\n')
    
# HTML backmatter
print('</table>\n')
print('</body>\n')
print('</html>\n')
