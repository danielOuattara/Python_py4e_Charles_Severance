"""Exercices on file open and exploiting the data"""

print(100 * "~")

#  Read the whole file :
with open("mail_box.txt", encoding="utf-8") as mail_box:
    print(mail_box.read())
    mail_box.close()

print(100 * "~")

#  Read the file Line by Line:
with open("mail_box.txt", encoding="utf-8") as mail_box:
    for line in mail_box:
        print(line)
    mail_box.close()

print(100 * "~")

#  Read the file Line by Line + line upper():
with open("mail_box.txt", encoding="utf-8") as mail_box:
    for line in mail_box:
        line = line.upper()
        print(line)
    mail_box.close()

print(100 * "~")

#  Read the file Line by Line, no new lines:
with open("mail_box.txt", encoding="utf-8") as mail_box:
    for line in mail_box:
        line = line.rstrip()
        print(line)
    mail_box.close()


print(100 * "~")

#  Read the file Line by Line, no new lines + Lines uppper():
with open("mail_box.txt", encoding="utf-8") as mail_box:
    for line in mail_box:
        line = line.rstrip().upper()
        print(line)
    mail_box.close()
