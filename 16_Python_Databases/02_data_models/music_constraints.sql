-- Python for Everybody Database Handout
-- *
-- https://www.py4e.com/lectures3/Pythonlearn-15-Database-Handout.txt
-- *
-- Download and Install: http://sqlitebrowser.org/
-- NOTE: constraints are required in SQLite whereas they are not in DBMS like MySQL, PostgreSQL, etc.
-- *
-- Multi-Table SQL:
-- *
CREATE TABLE
  "Artist" ("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, "name" TEXT);

CREATE TABLE
  "Album" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    "artist_id" INTEGER,
    "title" TEXT,
    FOREIGN KEY (artist_id) REFERENCES Artist (id)
  );

CREATE TABLE
  "Genre" ("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, "name" TEXT);

CREATE TABLE
  "Track" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    "album_id" INTEGER,
    "genre_id" INTEGER,
    "len" INTEGER,
    "rating" INTEGER,
    "title" TEXT,
    "count" INTEGER,
    FOREIGN KEY (album_id) REFERENCES Album (id),
    FOREIGN KEY (genre_id) REFERENCES Genre (id)
  );

INSERT INTO
  Artist (name)
VALUES
  ('Led Zeppelin');

INSERT INTO
  Artist (name)
VALUES
  ('AC/DC');

INSERT INTO
  Genre (name)
VALUES
  ('Rock');

INSERT INTO
  Genre (name)
VALUES
  ('Metal');

INSERT INTO
  Album (title, artist_id)
VALUES
  ('Who Made Who', 2);

INSERT INTO
  Album (title, artist_id)
VALUES
  ('IV', 1);

INSERT INTO
  Track (title, rating, len, count, album_id, genre_id)
VALUES
  ('Black Dog', 5, 297, 0, 2, 1);

INSERT INTO
  Track (title, rating, len, count, album_id, genre_id)
VALUES
  ('Stairway', 5, 482, 0, 2, 1);

INSERT INTO
  Track (title, rating, len, count, album_id, genre_id)
VALUES
  ('About to Rock', 5, 313, 0, 1, 2);

INSERT INTO
  Track (title, rating, len, count, album_id, genre_id)
VALUES
  ('Who Made Who', 5, 207, 0, 1, 2);

SELECT
  Album.title,
  Artist.name
FROM
  Album
  JOIN Artist ON Album.artist_id = Artist.id;

SELECT
  Track.title,
  Genre.name
FROM
  Track
  JOIN Genre ON Track.genre_id = Genre.id;

SELECT
  Track.title,
  Artist.name,
  Album.title,
  Genre.name
FROM
  Track
  JOIN Genre ON Track.genre_id = Genre.id
  JOIN Album ON Track.album_id = Album.id
  JOIN Artist ON Album.artist_id = Artist.id;