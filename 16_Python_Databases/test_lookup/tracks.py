import xml.etree.ElementTree as ET

#  print(dir(ET))
#  print(help(ET))

<<<<<<< HEAD
filename = open('./Library.xml')
=======
filename = open('Library.xml')
>>>>>>> b3f7c80 (Committing local changes before pulling from remote)
playlist = ET.parse(filename)
all = playlist.findall('dict/dict/dict')


# print('Dict count:', len(all))
#
# print("dict[0] = ", all[0])
# for item in all[0]:
#     print('\t', "item = ", item.tag, item.text)


def lookup(d, value):
    found = False
    for child in d:
        print("found = ", found)
        if found:
            return child.text
        if child.tag == 'key' and child.text == value:
            found = True
    return None


# for entry in all:
#     print(lookup(entry, 'Track ID'))
#     if lookup(entry, 'Track ID') is None:
#         print('Track id not found !')
#         continue
#     name = lookup(entry, 'Name')
#     artist = lookup(entry, 'Artist')
#     album = lookup(entry, 'Album')
#     count = lookup(entry, 'Play Count')
#     rating = lookup(entry, 'Rating')
#     length = lookup(entry, 'Total Time')
#
#     print(name, artist, album, count, rating, length, '\n')


for entry in all:
    print(lookup(entry, 'Track ID'))
