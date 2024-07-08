name = input("Enter file:")
if len(name) < 1:
    name = "mail_box.txt"
file = open(name)

counts = {}
greater_value = 0
greater_key = None

for line in file:
    if not line.startswith('Author'):
        continue
    words = line.strip().split()
    # print(words)
    counts[words[1]] = counts.get(words[1], 0) + 1

    for key, value in counts.items():
        if value > greater_value:
            greater_value = value
            greater_key = key

print(f'counts =  {counts}')
print(greater_key, greater_value)

# --------------------------------------------------

filename = input("Enter file:")
if len(filename) < 1:
    filename = "mail_box.txt"

counts = {}
greater_value = 0
greater_key = None

with open(name) as file:
    for line in file:
        if line.startswith('Author'):
            words = line.strip().split()
            counts[words[1]] = counts.get(words[1], 0) + 1

        for key, value in counts.items():
            if value > greater_value:
                greater_value = value
                greater_key = key
print(greater_key, greater_value)
