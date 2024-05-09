import xml.etree.ElementTree as ET
import xml.dom
import xml.parsers
import xml.sax
import xml.etree

# print(help(xml.dom))
# print(help(xml.parsers))
# print(help(xml.sax))
# print(help(xml.etree))
print(help(ET))

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

data_xml = ET.fromstring(data)
print('Name:', data_xml.find('name').text)
print('Phone:', data_xml.find('phone').text)
print('Attr:', data_xml.find('email').get('hide'))
