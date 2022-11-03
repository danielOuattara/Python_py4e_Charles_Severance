import re

file = open("./assignment_regex.txt")
total = 0
for line in file:
    line = line.strip()
    numbers = re.findall("([0-9]+)", line)
    if len(numbers) == 0:
        continue
    for number in numbers:
        total += int(number)

print(total)

print(70 * "~", "\n")
# -------------------------------------------------------------


file = open("./assignment_regex.txt")
total = 0
numbers_list = list()
for line in file:
    line = line.strip()
    numbers = re.findall("([0-9]+)", line)
    if len(numbers) == 0:
        continue
    for number in numbers:
        total += float(number)
        numbers_list.append(int(number))

print(total)
print(numbers_list)
print("Maximum:", max(numbers_list))
print("Mean Value: ", total / len(numbers_list))

print(70 * "~", "\n")
# --------------------------------------------------------------

#  [item for item in line_clean if item != ""]

print(sum([int(number) for number in re.findall('[0-9]+', open("./assignment_regex.txt").read())]))
