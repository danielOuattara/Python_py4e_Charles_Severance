"""Auto-grader 1"""


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

# ----------------------------------------------------

try:
    file_name = input("Enter file name: ")
except FileNotFoundError as err:
    print(err)

list_words = []
with open(file=file_name, encoding='utf-8') as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            if word not in list_words:
                list_words.append(word)

list_words.sort()
print(list_words)
