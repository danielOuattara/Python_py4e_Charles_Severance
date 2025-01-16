"""Use the file name mbox-short.txt as the file name"""

# auto-grader Code version 1
fname = input("Enter file name: ")
count = 0
total = 0
f_h = open(fname)
for line in f_h:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    new_line = line.split()
    total += float(new_line[1])
    count += 1

print("Average spam confidence:", total / count)

# ---------------------------------------------------

# auto-grader Code version 2
fname = input("Enter file name: ")
count = 0
total = 0

with open(fname, encoding="utf-8") as f_h:
    for line in f_h:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        new_line = line.split()
        total += float(new_line[1])
        count += 1

print("Average spam confidence:", total / count)
