# (c) 2021 Open Risk (https://www.openriskmanagement.com)

import owlready2 as owl
import inspect
import pprint as pp

# onto = owl.get_ontology('cro.owl').load()
# Alternatively load graph data from a URL
onto = owl.get_ontology('https://www.openriskmanual.org/ns/cro/ontology.xml').load()

New_CRA = onto.CreditRatingAgency("ESMA_ID", has_agency_description=["A description"])
New_CRA.has_webpage = ["https://example.com"]
New_CRA.has_name = ['CRA Name']
New_CRA.has_new_property = 'My Property'

print("Members of the live New_CRA object")
pp.pprint(inspect.getmembers(New_CRA))

print("Type of OWL properties")
for elem in dir(New_CRA):
    try:
        print(elem, type(New_CRA.__getattr__(elem)))
    except Exception as e:
        pass