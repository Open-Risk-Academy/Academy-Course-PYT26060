# (c) 2021 - 2022 Open Risk (https://www.openriskmanagement.com)

import json
import owlready2 as owl
from custom_datatypes import *

# Load our ontology and any custom datatypes
# onto = owl.get_ontology('cro.owl').load()
# Alternatively load graph data from a URL
onto = owl.get_ontology('https://www.openriskmanual.org/ns/cro/ontology.xml').load()
owl.declare_datatype(URL, "https://www.w3.org/2001/xmlschema#anyURI", parser, unparser)

# Load our JSON data file
data = json.load(open('ecai_list.json', mode='r'))

# Iterate over the list
for item in data:
    name = item['has_ESMA_id']
    # Create an object representing the CRA
    New_CRA = onto.CreditRatingAgency(name)
    # Add properties representing the available CRA attributes (standard string type)
    New_CRA.has_name = [item['has_name']]
    New_CRA.has_agency_description = [item['has_agency_description']]
    New_CRA.has_methodology_description = [item['has_methodology_description']]
    # Add properties representing the available CRA attributes (Note: this is a custom URL type)
    New_CRA.has_webpage = [URL(item['has_webpage'])]
    New_CRA.has_methodology_url = [URL(item['has_methodology_url'])]

# Write the graph into a file using the XML format
onto.save(file="ecai_list.owl", format="rdfxml")
