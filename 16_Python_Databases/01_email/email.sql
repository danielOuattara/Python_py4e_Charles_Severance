-- Python for Everybody Database Handout
-- /
-- https://www.py4e.com/lectures3/Pythonlearn-15-Database-Handout.txt
-- /
-- Download and Install: http://sqlitebrowser.org/
-- Single Table SQL
CREATE TABLE
    "Users" ("name" TEXT, "email" TEXT);

INSERT INTO
    Users (name, email)
VALUES
    ('Chuck', 'csev@umich.edu'),
    ('Colleen', 'cvl@umich.edu'),
    ('Ted', 'ted@umich.edu'),
    ('Sally', 'a1@umich.edu'),
    ('Ted', 'ted@umich.edu'),
    ('Kristen', 'kf@umich.edu');

DELETE FROM Users
WHERE
    email = 'ted@umich.edu';

UPDATE Users
SET
    name = "Charles"
WHERE
    email = 'csev@umich.edu';

SELECT
    *
FROM
    Users;

SELECT
    *
FROM
    Users
WHERE
    email = 'csev@umich.edu';

SELECT
    *
FROM
    Users
ORDER BY
    email;

SELECT
    *
FROM
    Users
ORDER BY
    name DESC;