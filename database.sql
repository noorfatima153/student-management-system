CREATE DATABASE student_management;
USE student_management;

CREATE TABLE admins(
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(50),
password VARCHAR(50)
);

INSERT INTO admins(username,password)
VALUES('admin','admin123');

CREATE TABLE students(
id INT AUTO_INCREMENT PRIMARY KEY,
student_id VARCHAR(20) UNIQUE,
name VARCHAR(100),
age INT,
department VARCHAR(100),
email VARCHAR(100),
cgpa DECIMAL(3,2)
);



