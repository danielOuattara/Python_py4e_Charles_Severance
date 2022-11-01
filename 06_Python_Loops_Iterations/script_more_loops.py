#  ----------------------------------------------

#  Counting in a Loop
total = 0
print('Start', total)
for item in [9, 41, 12, 3, 74, 15]:
    total = total + 1
    print('item = ', item, ', total = ', total)

print('End', total)

print(70 * '-')

#  ----------------------------------------------

#  Summing list items
sum = 0
print('start', sum)
for item in [9, 41, 12, 3, 74, 15]:
    sum += item
    print('item = ', item, ', sum = ', sum)

print('End', sum)

print(70 * '-')

#  ----------------------------------------------

#  Finding the Average in a Loop
average = 0
sum = 0
total_items = 0
print('start, Average = ', average)
for item in [9, 41, 12, 3, 74, 15]:
    sum += item
    total_items = total_items + 1

average = sum / total_items

print('End, Average = ', average)

print(70 * '-')

#  ----------------------------------------------

# Filtering in a loop
print('start')

new_list = []
for item in [9, 41, 12, 3, 74, 15]:
    if item > 20:
        new_list.append(item)

print('End', new_list)

print(70 * '-')

number_list = [9, 41, 12, 74, 3, 15, 3]
new_list = [item for item in number_list if item > 20]
print(new_list)
#  newlist = [x for x in fruits if x != "banana"]

print(70 * '-')

#  ----------------------------------------------

# Searching Using Boolean Variable
item_found = False
index_list = []
items_list = []
print('start', item_found)
for item in number_list:
    if item % 3 == 0:
        item_found = True
        index_list.append(number_list.index(item))
        items_list.append(item)
    else:
        item_found = False
print("item_list = ", items_list, '\n', "index_list = ", index_list)

print(70 * '-')

#  ----------------------------------------------

# same as above but  SHORTER !!!
found_list = [item for item in number_list if item % 3 == 0]
index_list = [number_list.index(item) for item in number_list if item % 3 == 0]
print("found_list = ", found_list, '\n',"index_list = ", index_list)

print(70 * '-')

#  ----------------------------------------------

# How to find the largest
largest_value = -float('inf')
print('start to find the largest')
for number in number_list:
    if number > largest_value:
        largest_value = number

print('final', largest_value)
print(70 * '-')

#  ----------------------------------------------

# How to find the smallest
smallest_value = float('inf')
print('start to find the smallest')
for number in number_list:
    if number < smallest_value:
        smallest_value = number

print('final', smallest_value)

print(70 * '-')

# The 'is' , 'is not' Operators
print(0 == 0.0)
#  print(0 is 0.0)
