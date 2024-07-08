import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
  <age>38</age>
</person>'''

tree_xml = ET.fromstring(data)
print(f'Name: {tree_xml.find("name").text}')
print(f'Attr: {tree_xml.find("email").get("hide")}')
print(f'Age: {tree_xml.find("age").text}')
