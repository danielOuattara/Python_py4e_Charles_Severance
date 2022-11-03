import re

data = "From stephen.marquard@uct.ac.za Fri Jan  4 04:07:34 2008"

# multi stages technic
at_position = data.find("@")
print(at_position)
space_position_after_at = data.find(" ", at_position)
print(space_position_after_at)
host_name = data[at_position + 1: space_position_after_at]
print(host_name)

# Split technic
words = data.split()
email = words[1]
email_split = email.split("@")
print(email_split[1])

# Same as above using RegEx
host_name = re.findall("@(\S+)", data)
print(host_name)

host_name = re.findall("@([^ ]*)", data)
print(host_name)

host_name = re.findall("^From.*@([^ ]*)", data)
print(host_name)

# Spam Confidence
file = open("mail_box.txt")
number_list = list()
number_median = 0

for line in file:
    line = line.strip()
    stuff = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line)
    if len(stuff) == 0:
        continue
    number = float(stuff[0])
    number_list.append(number)
    number_median += number
print("Maximum:", max(number_list))
print("Mean Value: ", number_median / len(number_list))

# Escape Character

"""
\$
\.
\?
"""
