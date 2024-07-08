# Version 1
# ----------

filename = input("Enter file:")
if len(filename) < 1:
    filename = "demo.txt"
file = open(filename)

hours_list = list()
for line in file:
    if not 'From' in line:
        continue
    words_list = line.strip().split()
    if len(words_list) < 3:
        continue
    time_list = words_list[5].split(':')
    hours_list.append(time_list[0])
file.close()

hours_dict = dict()
for item in hours_list:
    hours_dict[item] = hours_dict.get(item, 0) + 1
for k, v in sorted(hours_dict.items()):
    print(k, v)


print('-------------------------------')
# Version 2
# ----------

filename = input("Enter file:")
if len(filename) < 1:
    filename = "demo.txt"

hours_list = list()
with open(filename) as file:
    for line in file:
        if 'From' in line:
            words_list = line.split()
            if len(words_list) > 3:
                time_list = words_list[5].split(':')
                hours_list.append(time_list[0])

hours_dict = dict()
for item in hours_list:
    hours_dict[item] = hours_dict.get(item, 0) + 1
for k, v in sorted(hours_dict.items()):
    print(k, v)


print('-------------------------------')
# Version 3
# ----------

filename = input("Enter file: ")
if not filename:
    filename = "demo.txt"

hours_dict = {}
with open(filename) as file:
    for line in file:
        if line.startswith('From '):
            words = line.split()
            if len(words) > 5:
                hour = words[5].split(':')[0]
                hours_dict[hour] = hours_dict.get(hour, 0) + 1

print(f'hours_dict = {hours_dict}')

hours_dict_sorted_increase = sorted(hours_dict.items())
print(hours_dict_sorted_increase)
# list hours & count decreasing
for (hour, count) in hours_dict_sorted_increase:
    print(hour, count)


hours_dict_sorted_decrease = sorted(hours_dict.items(), key=lambda item: item[1], reverse=True)
print(hours_dict_sorted_decrease)
# list hours & count decreasing
for (hour, count) in hours_dict_sorted_decrease:
    print(hour, count)
