""" Regex assignment: multiple solutions"""

import re

total = 0
with open("assignment_regex.txt", encoding='utf-8') as file:
    for line in file:
        numbers = re.findall("([0-9]+)", line)
        if len(numbers) == 0:
            continue
        for number in numbers:
            total += int(number)
file.close()
print(total)

print(70 * "~", "\n")
# -------------------------------------------------------------

total = 0
numbers_list = list()
with open("assignment_regex.txt", encoding='utf-8') as file:
    for line in file:
        numbers = re.findall("([0-9]+)", line)
        if len(numbers) == 0:
            continue
        for number in numbers:
            total += float(number)
            numbers_list.append(int(number))
file.close()
print(total)
print(numbers_list)
print("Maximum:", max(numbers_list))
print("Mean Value: ", total / len(numbers_list))

print(70 * "~", "\n")
# --------------------------------------------------------------

#  [item for item in line_clean if item != ""]

# print(sum([int(number) for number in re.findall(
#     '[0-9]+', open("assignment_regex.txt").read())]))

print(sum([int(number) for number in re.findall(
    '[0-9]+', open("assignment_regex.txt").read())]))

print(70 * "~", "\n")
# ----------------------------------------------------------------


def number_summer():
    """
    Open a file and return its content. If file not 
    found print the error message and return None.

    Parse the content from a file to sum all the number 
    it finds there and return the result or None
    """

    file_content = ""
    try:
        with open("assignment_regex.txt", encoding='utf-8') as file:
            file_content = file.read()
            file.close()
    except FileNotFoundError as err:
        print(err)
        return None
    total = 0
    numbers = re.findall("([0-9]+)", file_content)
    for number in numbers:
        total = sum(int(number) for number in numbers)
    print(total)


number_summer()
print(70 * "~", "\n")

# ----------------------------------------------------------------


def file_reader():
    """
    Open a file and return its content. If file not 
    found print the error message and return None
    """
    try:
        with open("assignment_regex.txt", encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError as err:
        print(err)
        return None


def number_summer_2():
    """
    Parse the content from a file to sum all the number 
    it finds there and return the result or None
    """
    total = 0
    file_content = file_reader()

    if not file_content:
        print("No content to process.")
        return None

    numbers = re.findall("([0-9]+)", file_content)

    total = sum(int(number) for number in numbers)
    print(total)


number_summer_2()
print(70 * "~", "\n")
