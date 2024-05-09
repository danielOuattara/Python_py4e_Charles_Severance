import re

<<<<<<< HEAD
file = open("./assignment_regex.txt")
=======
file = open("assignment_regex.txt")
>>>>>>> b3f7c80 (Committing local changes before pulling from remote)
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


<<<<<<< HEAD
file = open("./assignment_regex.txt")
=======
file = open("assignment_regex.txt")
>>>>>>> b3f7c80 (Committing local changes before pulling from remote)
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

<<<<<<< HEAD
print(sum([int(number) for number in re.findall('[0-9]+', open("./assignment_regex.txt").read())]))
=======
print(sum([int(number) for number in re.findall('[0-9]+', open("assignment_regex.txt").read())]))
>>>>>>> b3f7c80 (Committing local changes before pulling from remote)
