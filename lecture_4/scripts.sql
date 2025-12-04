-- Table for students (student's id, full name, birth year).
CREATE TABLE IF NOT EXISTS students (
	id INTEGER PRIMARY KEY,
	full_name TEXT,
	birth_year INTEGER
);

-- Table for students' grades (grade's id, student's id(foreign key from table "students"), subject's name, grade).
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject TEXT,
    grade INTEGER CHECK(grade BETWEEN 1 AND 100),
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- Insert student records (full name, birth year).
INSERT INTO students (full_name, birth_year) VALUES
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);

-- Insert grade records (student's id, subject, grade).
INSERT INTO grades (student_id, subject, grade) VALUES
(1, 'Math', 88), 
(1, 'English', 92), 
(1, 'Science', 85),
(2, 'Math', 75), 
(2, 'History', 83), 
(2, 'English', 79),
(3, 'Science', 95), 
(3, 'Math', 91), 
(3, 'Art', 89),
(4, 'Math', 84),
(4, 'Science', 88),
(4, 'Physical Education', 93),
(5, 'English', 90), 
(5, 'History', 85), 
(5, 'Math', 88),
(6, 'Science', 72), 
(6, 'Math', 78), 
(6, 'English', 81),
(7, 'Art', 94), 
(7, 'Science', 87), 
(7, 'Math', 90),
(8, 'History', 77), 
(8, 'Math', 83), 
(8, 'Science', 80),
(9, 'English', 96), 
(9, 'Math', 89), 
(9, 'Art', 92);

-- Finding all grades for Alice Johnson.
SELECT s.full_name, g.subject, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.full_name = 'Alice Johnson';

-- Calculate average grade per student.
SELECT s.full_name, ROUND(AVG(g.grade), 2) as average_grade
FROM students s
JOIN grades g on s.id = g.student_id
GROUP BY s.id
ORDER BY average_grade DESC, s.full_name;

-- List students born after 2004.
SELECT full_name, birth_year
FROM students
WHERE birth_year > 2004
ORDER BY birth_year, full_name;

-- Calculate average grade per subject.
SELECT subject, ROUND(AVG(grade)) as average_grade
FROM grades
GROUP BY subject
ORDER BY average_grade DESC, subject;

-- Find the top 3 students with the highest average grades.
SELECT s.full_name, ROUND(AVG(g.grade)) as  average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id
ORDER BY average_grade DESC, s.full_name
LIMIT 3;

-- List all students who have at least one grade below 80.
SELECT DISTINCT s.full_name
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80
ORDER BY s.full_name;