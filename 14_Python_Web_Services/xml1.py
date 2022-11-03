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

data_xml = ET.fromstring(data)
print('Name:', data_xml.find('name').text)
print('Attr:', data_xml.find('email').get('hide'))
print('Age:', data_xml.find('age').text)
