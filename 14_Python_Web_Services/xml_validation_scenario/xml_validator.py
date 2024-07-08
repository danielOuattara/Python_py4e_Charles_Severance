from lxml import etree

# Load the XML schema

with open('./schema.xsd', 'rb') as schema_file:
    schema_root = etree.XML(schema_file.read())
    schema = etree.XMLSchema(schema_root)

# Parse the XML Document

with open('./document.xml', 'rb') as xml_file:
    xml_doc = etree.XML(xml_file.read())


# Validation of the XML document against the schema

if schema.validate(xml_doc):
    print("XML document is valid.")
else:
    print("XML document is invalid.")
    for error in schema.error_log:
        print(error.message)
