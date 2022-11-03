 -- INSERT INTO 
-- 	TABLE_NAME [(column1, column2, column3,...columnN)]  
-- 	VALUES (value1, value2, value3,...valueN);
-- INSERT INTO TABLE_NAME VALUES (value1,value2,value3,...valueN);
sqlite >
CREATE TABLE
  COMPANY (
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(50),
    SALARY REAL
  );

INSERT INTO
  COMPANY (ID, NAME, AGE, ADDRESS, SALARY)
VALUES
  (1, 'Paul', 32, 'California', 20000.00);

INSERT INTO
  COMPANY (ID, NAME, AGE, ADDRESS, SALARY)
VALUES
  (2, 'Allen', 25, 'Texas', 15000.00);

INSERT INTO
  COMPANY (ID, NAME, AGE, ADDRESS, SALARY)
VALUES
  (3, 'Teddy', 23, 'Norway', 20000.00);

INSERT INTO
  COMPANY (ID, NAME, AGE, ADDRESS, SALARY)
VALUES
  (4, 'Mark', 25, 'Rich-Mond ', 65000.00),
  (5, 'David', 27, 'Texas', 85000.00),
  (6, 'Kim', 22, 'South-Hall', 45000.00);

INSERT INTO
  COMPANY
VALUES
  (7, 'James', 24, 'Houston', 10000.00);