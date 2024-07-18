import sqlite3

url = input('Enter file name: ')
if len(url) < 1:
    url = 'mbox.txt'

try:
    file_handle = open(url)
except:
    print("Not found")
    exit()

conn = sqlite3.connect('emails.sqlite')
cursor = conn.cursor()

cursor.execute('''DROP TABLE IF EXISTS Counts''')
cursor.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

for line in file_handle:
    if not line.startswith('From: '):
        continue
    words = line.split()
    email = words[1]
    org = email.split('@')[1]

    cursor.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cursor.fetchone()

    if row:
        cursor.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    else:
        cursor.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))

    conn.commit()

sql = 'SELECT org, count FROM Counts ORDER BY count DESC'
for row in cursor.execute(sql):
    print(str(row[0]), row[1])

cursor.close()
