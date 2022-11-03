import re

x = "My 2 favorite numbers are 19 and 42"

y = re.findall(r"[0-9]", x)
print(y)
print()

y = re.findall(r"[0-9]+", x)
print(y)
print()

y = re.findall(r"\d+", x)
print(y)
print()

y = re.findall(r"[AEYUIO]+", x)
print(y)
print()

# Greedy Matching
line = "From: Using the : character mail"
y = re.findall("^F.+:", line)
if y:
    print(y)

# Non-Greedy Matching
line = "From: Using the : character mail"
y = re.findall("^F.+?:", line)
if y:
    print(y)

# Fine Tune String Extraction

x = "From stephen.marquard@uct.ac.za Fri Jan  4 04:07:34 2008"
y = re.findall("\S+@\S+", x)
print(y)

y = re.findall("^From \S+@\S+", x)
print(y)

y = re.findall("^From (\S+@\S+)", x)
print(y)
