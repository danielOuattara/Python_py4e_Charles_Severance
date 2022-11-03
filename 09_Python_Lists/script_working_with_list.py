print(70 * '-')

# Concatenating
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print("c = ", c)

# print(help(list))

a.extend(b)
print("a = ", a)  # None ???

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
print(items)

items.append("cookie")
print(items)

print(70 * '-')

# in Operator
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)
print(7 in numbers)
print(7 not in numbers)

# Order lists
items = ['book', 'western', 'cookie']
items.sort()
print(items)

numbers = [3, 1, 5, 3, 4]
numbers.sort()
print(numbers)
print(70 * '-')

# Working with list

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
