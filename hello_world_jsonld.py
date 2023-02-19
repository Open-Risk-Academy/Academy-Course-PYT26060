# (c) 2021 - 2023 Open Risk (https://www.openriskmanagement.com)

from rdflib import Graph

# Create an new RDF graph
g = Graph()
# Load graph data from a file
# g.load('cro.owl')
# Alternatively load graph data from a URL
g.load('https://www.openriskmanual.org/ns/cro/ontology.xml')

# Define our semantic context
context = {"@language": "en",
           "@cro": "https://www.openriskmanual.org/ns/cro/",
           "@owl": "http://www.w3.org/2002/07/owl#",
           "@rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
           "@rdfs": "http://www.w3.org/2000/01/rdf-schema#",
           "@xsd": "http://www.w3.org/2001/XMLSchema#"
           }

# Convert the ontology from xml format to json format
f = open("cro.json", "w")
f.write(g.serialize(format='json-ld', context=context, indent=4).decode("utf-8"))
f.close()
