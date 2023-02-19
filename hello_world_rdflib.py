# (c) 2021 - 2023 Open Risk (https://www.openriskmanagement.com)

# hello_world_rdflib.py
import rdflib

# Create an new RDF graph
g = rdflib.Graph()
# Load graph data from a file
g.load('cro.owl')
# Alternatively load graph data from a URL
# g.load('https://www.openriskmanual.org/ns/cro/ontology.xml')

# Print the triples embedded in the graph
# s -> subject
# p -> predicate
# o -> object

for s, p, o in g:
    print(80 * '-')
    print(s, p, o)
