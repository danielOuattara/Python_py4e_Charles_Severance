import re

# ----- Matching & extract

x = "My 2 favorite numbers are 19 and 42"

y = re.findall(r"[0-9]", x)
print(y, '\n')

y = re.findall(r"[0-9]+", x)
print(y, '\n')

y = re.findall(r"\d+", x)
print(y, '\n')

y = re.findall(r"[AEYUIO]+", x)
print(y, '\n')

# ----- Greedy Matching

line = "From: Using the : character mail"
y = re.findall(r"^F.+:", line)
if y:
    print(y, '\n')

# ----- Non-Greedy Matching

line = "From: Using the : character mail"
y = re.findall(r"^F.+?:", line)
if y:
    print(y, '\n')

# ----- Fine Tune String Extraction

x = "From stephen.marquard@uct.ac.za Fri Jan  4 04:07:34 2008"
y = re.findall(r"\S+@\S+", x)
print(y, '\n')

y = re.findall(r"^From \S+@\S+", x)
print(y, '\n')

# Parentheses are not part of the match -
# but they tell where to start and stop what string to extract
y = re.findall(r"^From\s(\S+@\S+)", x)
print(y, '\n')
