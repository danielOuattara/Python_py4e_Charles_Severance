"""String and List"""

print(70 * '-')

# print(help(str))

print(70 * '-')

abc = "With three words"
print(abc)
print(70 * '-')

# split() method:
abc_list = abc.split()

print(abc_list)
print(len(abc_list))
print(abc_list[2])

print(70 * '-')

line = "A lot      of   spaces"
line_clean = line.split(sep=" ")
print(line_clean)

# -----------------------------
new_line_clean = list()
for item in line_clean:
    if item != "":
        new_line_clean.append(item)

print("new_line_clean = ",  new_line_clean)

# -----------------------------
new_line_clean_2 = [item for item in line_clean if item != ""]
print("new_line_clean_2 = ", new_line_clean_2)

# -----------------------------
line_clean_2 = line.split()
print(line_clean_2)

print(70 * '-')

line = "first;second;third"
new_line = line.split()
print(new_line)
print(len(new_line))

print(70 * '-')

line = "first;second;third"
new_line = line.split(";")
print(new_line)
print(len(new_line))

print(70 * '-')
