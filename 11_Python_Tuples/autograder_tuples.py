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

hours_dict = dict()
for item in hours_list:
    hours_dict[item] = hours_dict.get(item, 0) + 1
for k, v in sorted(hours_dict.items()):
    print(k, v)
