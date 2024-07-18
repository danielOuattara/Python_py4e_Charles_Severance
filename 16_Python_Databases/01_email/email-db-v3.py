import sqlite3

filename = input('Enter file name: ')
if len(filename) < 1:
    filename = 'mail-box.txt'

with open(filename) as file:
    with sqlite3.connect('email-database.sqlite') as connection:
        cursor = connection.cursor()
        cursor.execute('''DROP TABLE IF EXISTS Counts''')
        cursor.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')

        for line in file:
            if line.startswith('From: '):
                pieces = line.split()
                email = pieces[1]

                cursor.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
                row = cursor.fetchone()
                if row is None:
                    cursor.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
                else:
                    cursor.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))

        connection.commit()

# https://www.sqlite.org/lang_select.html
query = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

with sqlite3.connect('email-database.sqlite') as connection:
    cursor = connection.cursor()
    for row in cursor.execute(query):
        print(str(row[0]), row[1])
