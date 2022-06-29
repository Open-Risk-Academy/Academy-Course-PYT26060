# (c) 2021 - 2022 Open Risk (https://www.openriskmanagement.com)

# filter_rdf_file.py
import rdflib

# Create an new RDF graph
g = rdflib.Graph()
# Load a graph from a local directory
g.load('cro.owl')

# Find all triples defining a RDF type that is an OWL Datatype Property
dtp = rdflib.term.URIRef('http://www.w3.org/2002/07/owl#DatatypeProperty')
for s, p, o in g.triples((None, rdflib.RDF.type, dtp)):
    print("{} is a {}".format(s, o))

# Find all triples defining as OWL (RDFS) domain a Credit Rating Agency class
cra = rdflib.term.URIRef('https://www.openriskmanual.org/ns/cro/CreditRatingAgency')
for s, p, o in g.triples((None, rdflib.RDFS.domain, cra)):
    print("{} has domain {}".format(s, o))
