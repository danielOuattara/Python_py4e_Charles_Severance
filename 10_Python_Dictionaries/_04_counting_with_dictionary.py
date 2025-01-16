""" Counting using dictionaries """

from collections import Counter

# counting and outputting dictionary

my_list = ["marquard", "cwen", "zhen", "csev", "zhen",
           "marquard", "marquard", "cwen", "zhen", "zhen"]

# method 1 : linear reasoning, using 2 for loops

list_count_1 = dict()
for item in my_list:
    list_count_1[item] = 0
for item in my_list:
    list_count_1[item] += 1

print("list_count_1 = ", list_count_1)
# list_count_1 =  {'marquard': 3, 'cwen': 2, 'zhen': 4, 'csev': 1}

# ----------------------------

# method 2: single for loop

list_count_2 = dict()
for item in my_list:
    if item not in list_count_2:
        list_count_2[item] = 1
    else:
        list_count_2[item] += 1

print("list_count_2 = ", list_count_2)

# -----------------------------

# method 3: using dictionary method

list_count_3 = dict()
for item in my_list:
    list_count_3[item] = list_count_3.get(item, 0) + 1
    # print("list_count_3 = ", list_count_3)

print("list_count_3 = ", list_count_3)

# ------------------------------

list_count_4 = Counter(my_list)
print("list_count_4 = ", list_count_4)
print(type(list_count_4))
# ------------------------------

counts = {'quincy': 1, 'mrugesh': 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))

# print(help(dict))
