CREATE TABLE groups (
    id INTEGER,
    title TEXT,
    PRIMARY KEY(id ASC)
);

INSERT INTO groups (title) VALUES ('518');

SELECT * FROM groups;

INSERT INTO groups (title)
VALUES
('519'), ('519st'), ('516');

SELECT * FROM groups;
SELECT title FROM groups;

SELECT * FROM groups
WHERE title='519';

SELECT * FROM groups
WHERE id > 2;

SELECT * FROM groups
WHERE title LIKE '51%';

SELECT * FROM groups
WHERE title LIKE '%st';

SELECT title FROM groups
WHERE id=3;

INSERT INTO groups (title) VALUES ('619а');
SELECT * FROM groups;

UPDATE groups
SET title = '519a'
WHERE id = 5;
SELECT * FROM groups;

BEGIN TRANSACTION;

UPDATE groups
SET title = '***';
SELECT * FROM groups;

ROLLBACK;

SELECT * FROM groups;
