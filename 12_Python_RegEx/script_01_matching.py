import re

# print(help(re))

print(70 * "~", "0", "\n")

# using find()
# ==========================

file = open("mail_box.txt")
for line in file:
    if line.find("From:") >= 0:
        line = line.strip()
        print(line)

print(70 * "~", "1", "\n")


# using re.search()
# ========================

file = open("mail_box.txt")
for line in file:
    if re.search("From:", line):
        line = line.strip()
        print(line)

print(70 * "~", "2", "\n")


# using re.search() like startswith()
# ==================================

file = open("mail_box.txt")
for line in file:
    if line.startswith("From:"):
        line = line.strip()
        print(line)

print(70 * "~", "3", "\n")

# ==================================
file = open("mail_box.txt")
for line in file:
    if re.search("^From:", line):
        line = line.strip()
        print(line)


print(70 * "~", "4", "\n")

# ==================================
file = open("mail_box.txt")

for line in file:
    if re.search("edu$", line):
        line = line.strip()
        print(line)

print(70 * "~", "5", "\n")

# ==================================
file = open("mail_box.txt")

for line in file:
    if re.search("^X.*:", line):
        line = line.strip()
        print(line)

print(70 * "~", "6", "\n")

# ==================================
file = open("mail_box.txt")

for line in file:
    if re.search("^X.+:", line):
        line = line.strip()
        print(line)

print(70 * "~", "7", "\n")

