"""Use the file name mbox-short.txt as the file name"""

fname = input("Enter file name: ")
count = 0
total = 0

with open(fname, encoding='utf-8') as fh:
    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        new_line = line.split()
        total += float(new_line[1])
        count += 1

print("Average spam confidence:", total / count)
