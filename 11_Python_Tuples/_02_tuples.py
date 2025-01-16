"""Tuples 2"""

# Sorting Lists of Tuples

print('------------------------------------', "1")

dic = {"a": 10, "z": 3, "c": 22, "b": 1}

# print dictionary
print("dic = ", dic)

# print dic.items()
print(f'dic.items() = {dic.items()}')

print('------------------------------------', "2")

# Sort by key
print(f'sorted(dic.items()) = {sorted(dic.items())}')

print('------------------------------------', "3")
# show key/value pairs
for k, v in sorted(dic.items()):
    print(k, v)


print('------------------------------------', "4")

# Sort by value

dic = {"a": 10, "b": 1, "c": 22}

tmp_list = list()
for (k, v) in dic.items():
    tmp_list.append((v, k))
print(f'tmp_list = {tmp_list}')

tmp_list = sorted(tmp_list, reverse=True)
print(f'tmp_list = {tmp_list}')

final_list = list()

for v, k in tmp_list:
    final_list.append((k, v))
print(f'final_list = {final_list}')

print('-------------', '')

# Sort by value : Optimized

dic = {"a": 10, "b": 1, "c": 22}

final_list_2 = sorted(dic.items(), key=lambda item: item[1], reverse=True)
print(f'final_list_2 = {final_list_2}')

print('------------------------------------', '5')

# Find The most used word in a text

file = open("demo.txt")
counts = dict()
for line in file:
    words = line.strip().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
file.close()

new_list = list()
for key, val in counts.items():
    new_tuple = (val, key)
    new_list.append(new_tuple)

new_list = sorted(new_list, reverse=True)

for val, key in new_list[: 10]:
    print(key, val)

print('------------------------------------', '6')

# Find The most used word in a text: Optimized

counts = {}
with open("demo.txt", encoding='utf-8') as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1
    file.close()
# Sort items by count in descending order
final_list_3 = sorted(counts.items(), key=lambda item: item[1], reverse=True)

# Print the top 10 words and their count
for word, count in final_list_3[: 10]:
    print(word, count)

print('------------------------------------', "7")


# Including comprehension list in the previous code

file = open("demo.txt")
counts = dict()
for line in file:
    words = line.strip().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

new_list = sorted([(v, k) for (k, v) in counts.items()], reverse=True)

for val, key in new_list[: 10]:
    print(key, val)

print('------------------------------------', '8')

# comprehension list again

dic_2 = {"a": 10, "z": 3, "c": 22, "b": 1}
print("dic_2 = ", dic_2)
print("dic_2_sorted = ", sorted(dic_2.items()))
print("dic_2_ordered_key = ", sorted([(k, v) for k, v in dic_2.items()]))
