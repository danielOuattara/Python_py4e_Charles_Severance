import sqlite3

connection = sqlite3.connect('email-database.sqlite')
cursor = connection.cursor()

cursor.execute('''DROP TABLE IF EXISTS Counts''')
cursor.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')

filename = input('Enter file name: ')
if len(filename) < 1:
    filename = 'mail-box.txt'

file_handle = open(filename)
for line in file_handle:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]

    cursor.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cursor.fetchone()

    if row is None:
        cursor.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    else:
        cursor.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                       (email,))
connection.commit()

# https://www.sqlite.org/lang_select.html
query = 'SELECT email, count FROM Counts ORDER BY count DESC'

for row in cursor.execute(query):
    print(str(row[0]), row[1])

cursor.close()

file_handle.close()