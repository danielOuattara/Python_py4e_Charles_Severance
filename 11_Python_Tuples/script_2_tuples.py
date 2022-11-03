# Sorting Lists of Tuples
print(70 * '-', "1")

dic = {"a": 10, "z": 3, "c": 22, "b": 1}
print("dic = ", dic)
print(dic.items())

print(70 * '-', "2")

# Sort by key
print(sorted(dic.items()))

# show key/value pairs
for k, v in sorted(dic.items()):
    print(k, v)

print(70 * '-', "3")

# Sort by value
dic = {"a": 10, "b": 1, "c": 22}
tmp_list = list()
for (k, v) in dic.items():
    tmp_list.append((v, k))
print(tmp_list)

tmp_list = sorted(tmp_list, reverse=True)
print(tmp_list)
final_list = list()

for v, k in tmp_list:
    final_list.append((k, v))
print(final_list)

print(70 * '-', '4')

# Find The most used word in a text
file = open("demo.txt")
counts = dict()
for line in file:
    words = line.strip().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

new_list = list()
for key, val in counts.items():
    new_tuple = (val, key)
    new_list.append(new_tuple)

new_list = sorted(new_list, reverse=True)

for val, key in new_list[: 10]:
    print(key, val)

print(70 * '-')

# Including comprehension list in the previous code

file = open("demo.txt")
counts = dict()
for line in file:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

new_list = sorted([(v, k) for (k, v) in counts.items()], reverse=True)

for val, key in new_list[: 10]:
    print(key, val)

# comprehension list again

dic_2 = {"a": 10, "z": 3, "c": 22, "b": 1}
print("dic_2 = ", dic_2)
print("dic_2_sorted = ", sorted(dic_2.items()))
print("dic_2_ordered_key = ", sorted([(k, v) for k, v in dic_2.items()]))
