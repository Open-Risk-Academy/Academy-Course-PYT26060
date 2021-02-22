# (c) 2021 Open Risk (https://www.openriskmanagement.com)

import rdflib

from pyshacl import validate

# Create an new SHACL graph
sg = rdflib.Graph()
sg.load('shacl_graph.ttl', format='ttl')

# Load the data to validate
dg = rdflib.Graph()
dg.load('ecai_list.owl')

r = validate(dg, shacl_graph=sg)
conforms, results_graph, results_text = r

print(results_text)