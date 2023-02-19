# (c) 2021 - 2023 Open Risk (https://www.openriskmanagement.com)

import json
from rdflib import Graph, Namespace
from rdflib import URIRef, Literal, RDF

# Load our JSON data file
data = json.load(open('ecai_list.json', mode='r'))

# Create an empty RDF graph
g = Graph()
cro = Namespace("https://www.openriskmanual.org/ns/cro/")
# Bind the namespace to our ontology
g.bind("cro", cro)

# Define our semantic context
context = {"@language": "en",
           "@cro": "https://www.openriskmanual.org/ns/cro/",
           "@owl": "http://www.w3.org/2002/07/owl#",
           "@rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
           "@rdfs": "http://www.w3.org/2000/01/rdf-schema#",
           "@xsd": "http://www.w3.org/2001/XMLSchema#"
           }

# Iterate over the list
for item in data:
    name = item['has_ESMA_id']
    # Add a triplet representing the CRA
    g.add((cro[name], RDF.type, cro.CreditRatingAgency))
    # Add triplets representing the available CRA attributes that are Literals
    g.add((cro[name], cro.has_name, Literal(item['has_name'])))
    g.add((cro[name], cro.has_agency_description, Literal(item['has_agency_description'])))
    g.add((cro[name], cro.has_methodology_description, Literal(item['has_methodology_description'])))
    # Add triplets representing the available CRA attributes that are URL's
    g.add((cro[name], cro.has_methodology_url, URIRef(item['has_methodology_url'])))
    g.add((cro[name], cro.has_webpage, URIRef(item['has_webpage'])))

# Write the graph into a file using the JSON-LD format
f = open("ecai_list_ld.json", "w")
f.write(g.serialize(format='json-ld', context=context, indent=4).decode("utf-8"))
f.close()
