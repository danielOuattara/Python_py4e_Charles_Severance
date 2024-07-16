import xml.etree.ElementTree as ET

""" Handle list in XML """


input = """
<stuff>
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
</stuff>
"""

tree_xml = ET.fromstring(input)
print("tree_xml = ", tree_xml)

userlist = tree_xml.findall('users/user')
print(f'User count: {len(userlist)}')
print(f'list = {userlist}')

for item in userlist:
    print(
        f"Name = {item.find('name').text}\nId = {item.find('id').text}\nAttribute = {item.get('x')}\n")
