""" Working with lists """

print(70 * '-')

# Concatenating
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print("c = ", c, '\n')

# print(help(list))

# extending `a` with `b`:
print('extending a with b : ')
a.extend(b)
print("a = ", a)  # OK

print(70 * '-')

# Slicing
print(c[1: 3])
print(c[2: 5])

print(70 * '-')

# List Methods
# print(dir(list))

# print(70 * '-')

items = list()
items.append("book")
items.append(99)
print("items = ", items)

items.append("cookie")
print("items = ", items)

print(70 * '-')

# in Operator:
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)
print(7 in numbers)
print(7 not in numbers)

# Order lists:
items = ['book', 'western', 'cookie']
items.sort()
print(items)

numbers = [3, 1, 5, 3, 4]
numbers.sort()
print(numbers)
print(70 * '-')


# built-in functions and lists:
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))
print(70 * '-')


# Working with variable: provide numbers and return average

total = 0
count = 0
while (True):
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average:', average)


# Working with list: provide numbers and return average
number_list = list()
while True:
    input_value = input("Enter a number: ")
    if input_value == "done":
        break
    try:
        input_value = float(input_value)
    except:
        print("Please, enter a number")
        continue
    number_list.append(input_value)

average = None
if len(number_list):
    average = sum(number_list) / len(number_list)

print("average = ", average)
print(70 * '-')


# Working with list Optimized: provide numbers and return average

number_list = []

while True:
    input_value = input("Enter a number: ")
    if input_value.lower() == "done":
        break
    try:
        number_list.append(float(input_value))
    except ValueError:
        print("Please enter a valid number.")

if number_list:
    average = sum(number_list) / len(number_list)
    print("Average =", average)
else:
    print("No numbers were entered.")
