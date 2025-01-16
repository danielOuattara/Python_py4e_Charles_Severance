"""
Write a program that read emails headers and
find the email address from each origin infos data

example: From louis@media.berkeley.edu Fri Jan 4 18:10:48 200
"""

file = open('mail_box.txt')

for line in file:
    if line.startswith("From"):
        email = line.strip().split()[1]
        parts = email.split('@')
        print('email: ', email, ', domain:', parts[1])


file.close()


print(70 * '-')


# --- BETTER : using 'with' for resource-allocating operations

with open('mail_box.txt', encoding="utf-8") as file:
    for line in file:
        if line.startswith("From"):
            email = line.strip().split()[1]
            parts = email.split('@')
            print('email: ', email, ', domain:', parts[1])
    file.close()
