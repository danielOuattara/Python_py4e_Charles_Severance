""" Regular expression: application """

import re
import statistics

data = "From stephen.marquard@uct.ac.za Fri Jan  4 04:07:34 2008"

# ==> Extracting a hostname using multi stages technic using

# 1: using find
at_position = data.find("@")
print(at_position)

space_position_after_at = data.find(" ", at_position)
print(space_position_after_at)

host_name = data[at_position + 1: space_position_after_at]
print("host_name = ", host_name)

# 2: double split pattern
words = data.split()
email = words[1]
email_split = email.split("@")
print(email_split[1])

# ===> Same as above using RegEx

# 1
host_name = re.findall(r"@(\S+)", data)
print("host_name = ", host_name)

# 2 [^ ] : means a set of non-blank character(s)
host_name = re.findall(r"@([^ ]*)", data)
print("host_name = ", host_name)

host_name = re.findall(r"^From\s.*@([^ ]*)", data)
print("host_name = ", host_name)

print('-' * 50)
# ----------- Spam Confidence V1

file = open("mail_box.txt")
number_list = list()
number_median = 0

for line in file:
    stuff = re.findall(r"^X-DSPAM-Confidence:\s([0-9.]+)", line)
    if len(stuff) == 0:
        continue
    number = float(stuff[0])
    number_list.append(number)
    number_median += number

print(f'number_list = {number_list}')
print("Maximum:", max(number_list))
print(f'number_list items = {len(number_list)}')
print("Mean Value: ", number_median / len(number_list))
file.close()

# ----------- Spam Confidence V2
print('-' * 50)

pattern = r"^X-DSPAM-Confidence:\s([0-9.]+)"
with open("mail_box.txt", encoding='utf-8') as file:
    number_list = list()
    number_median = 0
    for line in file:
        if re.search(pattern, line):
            stuff = re.findall(pattern, line)
            number_list.append(float(stuff[0]))
            number_median += float(stuff[0])
file.close()
print(f'number_list = {number_list}')
print("Maximum:", max(number_list))
print("Mean Value: ", number_median / len(number_list))

# ----------- Spam Confidence V3
print('-' * 30)
number_list = []
with open("mail_box.txt", encoding='utf-8') as file:
    for line in file:
        match = re.findall(r"^X-DSPAM-Confidence:\s([0-9.]+)", line)
        if match:
            number = float(match[0])
            number_list.append(number)
file.close()

if number_list:
    number_mean = sum(number_list) / len(number_list)
    print(f'number_list = {number_list}')
    print("Maximum:", max(number_list))
    print("Mean Value:", number_mean)
    print("Median Value:", statistics.median(number_list))
else:
    print("No numbers found.")

# ----------- Spam Confidence V4
print('-' * 30)
pattern = r"^X-DSPAM-Confidence:\s([0-9.]+)"

with open("mail_box.txt", encoding='utf-8') as file:
    number_list = []
    for line in file:
        match = re.findall(pattern, line)
        if match:
            number_list.append(float(match[0]))

file.close()
if number_list:
    number_mean = sum(number_list) / len(number_list)
    print(f'number_list = {number_list}')
    print("Maximum:", max(number_list))
    print("Mean Value:", number_mean)
    print("Median Value:", statistics.median(number_list))
else:
    print("No numbers found.")

# ----------- Escape Character
print('-' * 50)
x = 'We just received $10,00 for cookies'

y = re.findall(r'\$[0-9]+', x)
print("y = ", y, '\n')

z = re.findall(r'\$[0-9.|,]+', x)
print("z = ", z, '\n')

"""
\$: 
\.
\?
"""
