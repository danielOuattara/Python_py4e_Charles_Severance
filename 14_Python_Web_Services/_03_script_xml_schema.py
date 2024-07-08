"""
# Many XML Schema Languages

1. Document Type Definition (DTD)
http://en.wikipedia.org/wiki/Document_Type_Definition

2. Standard Generalized Markup Language (ISO 8879:1986 SGML)
http://en.wikipedia.org/wiki/SGML

3. XML Schema  from W3C - (XSD)
http://en.wikipedia.org/wiki/XML_Schema_(W3C)


-> We will focus on the World Wide Web Consortium (W3C) version
-> It is often called “W3C Schema” because “Schema” is considered generic
-> More commonly it is called XSD because the file names end in .xsd


XML Schema Contract: XSD
-------------------------
<xs:complexType name=”person”>
  <xs:sequence>
    <xs:element name="lastname" type="xs:string"/>
    <xs:element name="age" type="xs:integer"/>
    <xs:element name="dateborn" type="xs:date"/>
   </xs:sequence>
</xs:complexType>

XML Document
--------------
<person>
   <lastname>Severance</lastname>
   <age>17</age>
   <dateborn>2001-04-17</dateborn>
</person>


XML Schema Contract: XSD + Constraints
----------------------------------------
<xs:element name="person">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="full_name" type="xs:string"
          minOccurs="1" maxOccurs="1" />
      <xs:element name="child_name" type="xs:string"
            minOccurs="0" maxOccurs="10" />
    </xs:sequence>
  </xs:complexType>
</xs:element>


XML Document
--------------
<person>
  <full_name>Tove Refsnes</full_name>
  <child_name>Hege</child_name>
  <child_name>Stale</child_name>
  <child_name>Jim</child_name>
  <child_name>Borge</child_name>
</person>


XSD Data Types
---------------
<xs:element name="customer" type="xs:string"/>
<xs:element name="start" type="xs:date"/>
<xs:element name="startdate" type="xs:dateTime"/>
<xs:element name="prize" type="xs:decimal"/>
<xs:element name="weeks" type="xs:integer"/>



<customer>John Smith</customer>
<start>2002-09-24</start>
<startdate>2002-05-30T09:30:10Z</startdate>
<prize>999.50</prize>
<weeks>30</weeks>

"""
# -----------------------------------------------

import xml.etree.ElementTree as ET

data = '''<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

print(70 * '-')
# -----------------------------------------------

data = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

tree_xml = ET.fromstring(data)
lst = tree_xml.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))

print(70 * '-')
