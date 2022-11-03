""" A simple web browser """

import urllib.error
import urllib.parse
import urllib.request

file_handle = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in file_handle:
    print(line.decode().strip())

#  Treat it Like a file
counts = dict()
file_handle = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in file_handle:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)

#  Reading Web page
file_handle = urllib.request.urlopen("https://www.youtube.com/")
for line in file_handle:
    print(line.decode().strip())

