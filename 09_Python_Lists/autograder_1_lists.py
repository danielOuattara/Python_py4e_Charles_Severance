file_name = input("Enter file name: ")
file = open(file_name)
list_words = list()
for line in file:
    line = line.strip()
    words = line.split()
    for word in words:
        if word not in list_words:
            list_words.append(word)

list_words.sort()
print(list_words)

