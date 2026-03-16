SELECT * FROM groups;

CREATE TABLE students (
    student_id INTEGER,
    first_name TEXT,
    last_name TEXT,
    group_id INTEGER,
    PRIMARY KEY (student_id ASC),
    FOREIGN KEY (group_id) REFERENCES groups(id)
);

INSERT INTO students (first_name, last_name, group_id)
VALUES
('Ivan', 'Shevchenko', 1),
('Ivan', 'Shevchenko', 2),
('Oleh', 'Ivanenko', 1),
('Olha', 'Shevcuk', 3),
('Oleksandr', 'Tarasenko', 2),
('Anton', 'Oleshko', 1),
('Maksym', 'Kohut', 3);

SELECT * FROM students;

SELECT students.first_name, students.last_name, students.group_id
FROM students;

SELECT s.first_name, s.last_name, s.group_id
FROM students AS s;

SELECT * FROM students AS s
JOIN groups g ON s.group_id = g.id;

SELECT s.first_name, s.last_name, g.title FROM students AS s
JOIN groups g ON s.group_id = g.id;

SELECT * FROM students s
JOIN groups g;

SELECT *
FROM students s
JOIN groups g ON s.group_id = g.id
ORDER BY g.id;

SELECT s.first_name, s.last_name, g.title
FROM students s
JOIN groups g ON s.group_id = g.id
ORDER BY g.id;
