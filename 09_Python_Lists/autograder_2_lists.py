file_name = input("Enter file name: ")
if len(file_name) < 1:
    file_name = "mail_box.txt"
file = open(file_name)
count = 0

for line in file:
    if not line.startswith("Author"):
        continue
    line = line.strip()
    words = line.split()
    print(words[1])
    count += 1

print("There were", count, "lines in the file with 'From' as the first word")

# -------------------------------------------------------------

file_name = input("Enter file name: ")
if len(file_name) < 1:
    file_name = "mail_box.txt"
count = 0

with open(file_name) as file:
    for line in file:
        if line.startswith("Author"):
            words = line.strip().split()
            print(words[1])
            count += 1

print("There were", count, "lines in the file with 'From' as the first word")
