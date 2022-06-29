# (c) 2021 - 2022 Open Risk (https://www.openriskmanagement.com)

import owlready2 as owl

# Load an ontology from a local file
# onto = owl.get_ontology('cro.owl').load()
# Alternatively load graph data from a URL
onto = owl.get_ontology('https://www.openriskmanual.org/ns/cro/ontology.xml').load()
print(type(onto))

# print all the classes of the ontology
print(80 * '=')
print('Ontology Classes')
print(80 * '-')
for c in onto.classes():
    print(c.name)

# print all the properties of the ontology
print(80 * '=')
print('Ontology Properties')
print(80 * '-')
for c in onto.properties():
    print(c.name)
