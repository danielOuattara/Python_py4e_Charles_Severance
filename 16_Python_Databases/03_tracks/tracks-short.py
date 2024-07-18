import xml.etree.ElementTree as ET
import sqlite3
from lookup import lookup
import sql

conn = sqlite3.connect('track_short_db-.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript(sql.sql_commands)

filename = input('Enter file name: ')
if len(filename) < 1:
    filename = 'library.xml'

playlist = ET.parse(filename)
all = playlist.findall('dict/dict/dict')

for entry in all:
    if lookup(entry, 'Track ID') is None:
        continue
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None:
        continue

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ? )''',
                (name, album_id, length, rating, count))

    conn.commit()
cur.close()
print('Done !')
