import re

# print(help(re))

print(70 * "~", "0", "\n")

# using find()
# ==========================

file = open("mail_box.txt")
for line in file:
    if line.find("From:") >= 0:
        print(line.strip())

file.close()

print(70 * "~", "1", "\n")

# using re.search()
# ========================

file = open("mail_box.txt")
for line in file:
    if re.search(r"From:", line):
        print(line.strip())

file.close()

print(70 * "~", "2", "\n")

# using re.search() like startswith()
# ==================================

file = open("mail_box.txt")
for line in file:
    if line.startswith("From:"):
        print(line.strip())

file.close()

print(70 * "~", "3", "\n")

# ==================================
file = open("mail_box.txt")
for line in file:
    if re.search(r"^From:", line):
        print(line.strip())

file.close()

print(70 * "~", "4", "\n")

# ==================================
file = open("mail_box.txt")

for line in file:
    if re.search(r"edu$", line):
        print(line.strip())

file.close()

print(70 * "~", "5", "\n")

# ==================================
# wild-card character
file = open("mail_box.txt")

for line in file:
    if re.search(r"^X.*:", line):
        print(line.strip())

file.close()

print(70 * "~", "6", "\n")

# -------------------
file = open("mail_box.txt")

for line in file:
    if re.search(r"^X.+:", line):
        print(line.strip())

file.close()

print(70 * "~", "7", "\n")

# ==================================
file = open("mail_box.txt")

for line in file:
    if re.search(r"^X-\S+:", line):
        print(line.strip())

file.close()

print(70 * "~", "8", "\n")
