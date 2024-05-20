# ----------------------------------------------

# Counting in a Loop
total = 0
print('Start', total)
for item in [9, 41, 12, 3, 74, 15]:
    total = total + 1
    print('item = ', item, ', total = ', total)

print('Count = ', total)

print(50 * '-')

# ----------------------------------------------

# Summing list items
sum_1 = 0
print('start', sum_1)
for item in [9, 41, 12, 3, 74, 15]:
    sum_1 += item
    print('item = ', item, ', sum = ', sum_1)

print('Total = ', sum_1)

print(50 * '-')

# ----------------------------------------------

# Finding the Average in a Loop
average = 0
sum_1 = 0
total_items = 0
print('start, Average = ', average)
for item in [9, 41, 12, 3, 74, 15]:
    sum_1 += item
    print("sum_1 = ", sum_1)

    total_items = total_items + 1
    print("total_items = ", total_items)

    average = sum_1 / total_items
    print("average = ", average)


print('End, Average = ', average)

print(50 * '-')

# ----------------------------------------------

# Filtering in a loop
print('start filtering : ')

new_list = []
for item in [9, 41, 12, 3, 74, 15, 23]:
    if item > 20:
        new_list.append(item)

print('End', new_list)

print(50 * '-')

# --------------

number_list = [9, 41, 12, 74, 3, 15, 3]
new_list = [item for item in number_list if item > 20]
print("new_list = ", new_list)

new_list_2 = [x for x in number_list if x != 41 and x != 74]
print("new_list_2 = ", new_list_2)

print(50 * '-')

# ----------------------------------------------

# Searching Using Boolean Variable

item_found = False
index_list = []
items_list = []
print('start Searching : ', item_found)
for item in number_list:
    if item % 3 == 0:
        item_found = True
        index_list.append(number_list.index(item))
        items_list.append(item)
    else:
        item_found = False
print("item_list = ", items_list, "\nindex_list = ", index_list)

print(50 * '-')

# -------------
# same as above but SHORTER code !

found_list = [item for item in number_list if item % 3 == 0]
index_list = [number_list.index(item) for item in number_list if item % 3 == 0]

print("found_list = ", found_list, '\n', "index_list = ", index_list)

print(50 * '-')

# ----------------------------------------------
# How to find the largest

largest_value = -float('inf')
print('start to find the largest')
for number in number_list:
    if number > largest_value:
        largest_value = number

print('final', largest_value)
print(50 * '-')

#  ----------------------------------------------
# How to find the smallest

smallest_value = float('inf')
print('start to find the smallest')
for number in number_list:
    if number < smallest_value:
        smallest_value = number

print('final', smallest_value)

print(50 * '-')

# The 'is' , 'is not' Operators
print(0 == 0.0)
# print(0 is 0.0)
