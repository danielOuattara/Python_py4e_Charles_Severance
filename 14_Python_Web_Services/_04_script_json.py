import json

# for item in dir(json):
#     print(item)

# print(help(json))

# --------------------------------------------------------------
print('\n', 70 * '-')

data = """
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   },
   "age": 38
}
"""

# json object TO python dictionary
info = json.loads(data)

print("type(info) = ", type(info))
print("info = ", info, '\n')

print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
print('Age:', info["age"])

print(70 * '-')
# --------------------------------------------------------------

data_2 = """
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]
"""

info_2 = json.loads(data_2)

print("type(info_2) = ", type(info_2))
print("info_2 = ", info_2, '\n')
print('User count:', len(info_2))

for item in info_2:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
    print(5 * '-')

print(70 * '-')
# --------------------------------------------------------------
