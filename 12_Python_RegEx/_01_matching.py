""" Regular expression: matching """

import re

# print(help(re))

print(70 * "~", "0", "\n")

# =====================================================

# using find()
with open("mail_box.txt", encoding='utf-8') as file:
    for line in file:
        if line.find("From:") >= 0:
            print(line.strip())
    file.close()

print(70 * "~", "1", "\n")

# using re.search()
with open("mail_box.txt", encoding='utf-8') as file:
    for line in file:
        if re.search(r"From:", line):
            print(line.strip())
    file.close()

print(70 * "~", "2", "\n")

# ======================================================

# using re.search() like startswith()
with open("mail_box.txt", encoding='utf-8') as file:
    for line in file:
        if line.startswith("From:"):
            print(line.strip())
    file.close()

print(70 * "~", "3", "\n")


# Matches the beginning of a line
with open("mail_box.txt", encoding='utf-8') as file:
    for line in file:
        if re.search(r"^From:", line):
            print(line.strip())
    file.close()

print(70 * "~", "4", "\n")

#  Matches the end of the line
with open("mail_box.txt", encoding='utf-8') as file:
    for line in file:
        if re.search(r"edu$", line):
            print(line.strip())
    file.close()

print(70 * "~", "5", "\n")

# ======================================================

# wild-card character
with open("mail_box.txt", encoding='utf-8') as file:
    for line in file:
        if re.search(r"^X.*:", line):
            print(line.strip())
    file.close()

print(70 * "~", "6", "\n")

# ---------------------------------
with open("mail_box.txt", encoding='utf-8') as file:
    for line in file:
        if re.search(r"^X.+:", line):
            print(line.strip())
    file.close()

print(70 * "~", "7", "\n")

# ---------------------------------
with open("mail_box.txt", encoding='utf-8') as file:
    for line in file:
        if re.search(r"^X-\S+:", line):
            print(line.strip())
    file.close()

print(70 * "~", "8", "\n")
