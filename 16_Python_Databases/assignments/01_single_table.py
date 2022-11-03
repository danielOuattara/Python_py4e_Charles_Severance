import sqlite3

conn = sqlite3.connect('single_table.sqlite')
cursor = conn.cursor()

cursor.executescript('''
DROP TABLE IF EXISTS Ages;

CREATE TABLE 
Ages ( 
  name VARCHAR(128), 
  age INTEGER
);

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Jun', 38);
INSERT INTO Ages (name, age) VALUES ('Briony', 25);
INSERT INTO Ages (name, age) VALUES ('Nathaniel', 31);
INSERT INTO Ages (name, age) VALUES ('Bronwen', 26);
INSERT INTO Ages (name, age) VALUES ('Harnek', 27);
INSERT INTO Ages (name, age) VALUES ('Courtney', 36);
''')

sql_str = 'SELECT hex(name || age) AS X FROM Ages ORDER BY X'
cursor.execute(sql_str)
result = cursor.fetchone()[0]
print("result = ", result)
cursor.close()
