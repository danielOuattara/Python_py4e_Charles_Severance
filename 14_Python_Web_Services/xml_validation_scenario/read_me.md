#  XML Validation

To perform XML validation in Python, you can use the `lxml` library,
which supports XML schema validation.

Below is a Python code example that demonstrates how to validate an
XML document against an XML Schema (XSD).

##  Step-by-Step Example

1- Install `lxml` Library:
You can install the lxml library using pip if you haven't already:

```sh
pip3 install lxml
```

2- Create the XML Schema (XSD):
Save the following XML Schema as schema.xsd:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="<http://www.w3.org/2001/XMLSchema">>
  <xs:element name="person">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="lastname" type="xs:string"/>
        <xs:element name="age" type="xs:integer"/>
        <xs:element name="dateborn" type="xs:date"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

3- Create the XML Document:
Save the following XML document as `document.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<person>
  <lastname>Severance</lastname>
  <age>17</age>
  <dateborn>2001-04-17</dateborn>
</person>
```

4- Python Code for Validation:

```python
from lxml import etree

# Load the XML Schema

with open('schema.xsd', 'r') as schema_file:
    schema_root = etree.XML(schema_file.read())
    schema = etree.XMLSchema(schema_root)

# Parse the XML document

with open('document.xml', 'r') as xml_file:
    xml_doc = etree.XML(xml_file.read())

# Validate the XML document against the schema

if schema.validate(xml_doc):
    print("XML document is valid.")
else:
    print("XML document is invalid.")
    for error in schema.error_log:
        print(error.message)
```

##  Explanation

- **Loading the XML Schema**

    The XML schema is read from `schema.xsd` and parsed into an `etree.XMLSchema` object.

- **Parsing the XML Document**

    The XML document is read from document.xml and parsed into an etree.XML object.

- **Validation**

    The validate method of the etree.XMLSchema object is used to validate the parsed XML document. If the document is invalid, the error messages are printed.

### Example Files Structure

```graphql
.
├── schema.xsd
├── document.xml
└── validate_xml.py
```

###  Running the Code

Make sure all files (schema.xsd, document.xml, and validate_xml.py) are in the same directory.

Run the validation script:

```sh
python validate_xml.py
```

This script will output whether the XML document is valid or invalid and print any validation errors encountered.
