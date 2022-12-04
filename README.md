## Resource Repository for the Open Risk Academy Course PYT 26060

![Semantic Python Logo](./SemanticPython.png)

* This repo collects resources (data and python scripts) used in the [course PYT26060](https://www.openriskacademy.com/course/view.php?id=60)
* It uses the [CRO Ontology Graph](https://www.openriskmanual.org/ns/cro/index-en.html) as the raw material to illustrate a number of Python tools for working with semantic data
* Discuss the course at the [Open Risk Commons](https://www.openriskcommons.org/t/overview-of-python-semantic-web-tools/62)

## Scripts

### Step 2
* hello_world_rdflib.py (load and parse a file containing rdf triples)
* explore_rdf_file.py (print out statistics about an rdf graph)
* filter_rdf_file.py (filter triples matching specific criteria)
* json_to_rdf.py (convert a json file to rdf)

### Step 3
* hello_world_owlready.py (loading, parsing and printing ontology properties)
* json_to_owl.py (convert a json file to owl class instances)

### Step 4
* hello_world_jsonld.py (convert an ontology form rdf/xml format to json-ld format)
* json_to_jsonld.py (convert a json file into a json-ld serialized set of owl class instances)

### Step 5
* hello_world_pyshacl.py (validate an OWL graph using a SHACL shape file)


## Data sets (only the input files - various files are created during the course)
* cro.owl an ontology file serialized in rdf/xml format
* ecai_list.json a json file with credit rating agency data (from ESMA)
* shacl_graph.ttl (a SHACL validation shape)


## DISCLAIMER

* The credit rating agency data sets included in this repo are actual published data obtained from [ESMA](https://www.esma.europa.eu/supervision/credit-rating-agencies/risk). They are only used here for educational purposes.


#### Where To Get Help:

If you get stuck on any issue with the course or the Academy:

- If the issue is related to the course topics / material, check in the first instance the Course Forum (Chat)
- Join the course discussion in the [Open Risk Commons](https://www.openriskcommons.org/t/overview-of-python-semantic-web-tools/62)
- If the issue is related the operation of the Open Risk Academy check first the Academy FAQ
- If the issue persists contact us at info at openrisk dot eu

## Academy Course Catalog

* [Course List and Description](https://www.openriskmanagement.com/academy-courses/)
