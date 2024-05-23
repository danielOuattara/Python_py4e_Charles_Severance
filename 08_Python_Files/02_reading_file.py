print(70 * "-")

# ----- File handle as a Sequence
file_handle = open("demo.txt")
for line in file_handle:
    print(line)

file_handle.close()
print(70 * "-")

# ----- Counting Number Of Lines In a File
file_handle = open("demo.txt")
count = 0
for line in file_handle:
    count += 1
print("Line count : ", count)

file_handle.close()

print(70 * "-")

# ------ Reading the Whole File
file = open("demo.txt")
file_itself = file.read()
print(len(file_itself))
print(file_itself)

file_handle.close()

print(70 * "-")

print(file_itself[: 140])

print(70 * "-")

# ----- Searching Through a File
file = open("demo.txt")
for line in file:
    if line.startswith("Line"):
        print(line)

file_handle.close()

print(70 * "-")

# ----- Searching Through a File, remove newline if any
file = open("demo.txt")
for line in file:
    if line.startswith("Line"):
        line = line.rstrip()
        print(line)

file_handle.close()

print(70 * "-")

# ----- Searching Through a File, remove newline if any + Skipping
#       not matching with Continue keyword
file = open("demo.txt")
for line in file:
    if not line.startswith("Line"):
        continue
    line = line.rstrip()
    print(line)

file_handle.close()

print(70 * "-")

# ----- Searching Through a File, remove newline if
#       any + Skipping not matching with "continue"
#       keyword + "in" operator

file = open("demo.txt")
for line in file:
    line = line.rstrip()
    if "Line" not in line:
        continue
    print(line)

file_handle.close()

print(70 * "-")

# ----- Prompt for File Name
file_name = input("Enter the file name: ")
print("-" * 3)
count = 0
file = open(file_name)
for line in file:
    if "Line" in line:
        count += 1

print("count = ", count)

file_handle.close()

print(70 * "-")

# ------ check For Prompted for File Name
file_name = input("Enter the file name: ")
print("-" * 3)
try:
    file = open(file_name)
except:
    print("File Not Found", file_name)
    quit()

count = 0
for line in file:
    if "Line" in line:
        count += 1

file.close()

print("count = ", count)

print(70 * "-")
