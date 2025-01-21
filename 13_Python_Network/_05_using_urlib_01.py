""" A simple web browser """

import urllib.error
import urllib.parse
import urllib.request

# ----- A simplest web browser

file_handle = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in file_handle:
    print(line.decode().strip())


# ----- Treat it Like a file


counts = dict()
file_handle = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in file_handle:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)


# ----- Reading Web page


file_handle = urllib.request.urlopen("https://www.youtube.com/")
for line in file_handle:
    print(line.decode().strip())


# ----- Storing Web page


result = ""
file_handle = urllib.request.urlopen("https://www.youtube.com/")
for line in file_handle:
    result += line.decode().strip()
    # print(result)
with open("./result.html", "w", encoding="utf-8") as file:
    file.write(result)
