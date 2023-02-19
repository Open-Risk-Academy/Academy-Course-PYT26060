# (c) 2021 - 2023 Open Risk (https://www.openriskmanagement.com)

# explore_rdf_file.py
import rdflib

# Create an new RDF graph
g = rdflib.Graph()
# Load a graph from a local directory
g.load('cro.owl')

# explore the RDF components

subjects = list(set([s for s in g.subjects()]))
print("Subjects: ", len(subjects))

predicates = list(set([p for p in g.predicates()]))
print("Predicates: ", len(predicates))

objects = list(set([o for o in g.objects()]))
print("Objects: ", len(objects))