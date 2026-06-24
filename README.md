# Student Management System

## Overview

Student Management System is a web-based application developed using Flask and MySQL. It allows administrators to manage student records through a simple and user-friendly interface. The system supports adding, viewing, searching, updating, and deleting student information while storing data securely in a MySQL database.

## Features

* Admin Login Authentication
* Add New Students
* View All Students
* Search Students
* Update Student Records
* Delete Student Records
* MySQL Database Integration
* Session-Based Authentication
* Simple Web Interface

## Technologies Used

* Python
* Flask
* MySQL
* mysql-connector-python
* HTML5
* CSS3

## Project Structure

```text
StudentManagementSystem/
│
├── student.py
├── database.sql
├── requirements.txt
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── add_student.html
│   └── update_student.html
│
└── README.md
```

## Database Schema

### Admin Table

Stores administrator login credentials.

### Students Table

Stores student information including:

* Student ID
* Name
* Age
* Department
* Email
* CGPA

## Functionalities

### Admin Login

Administrators must log in before accessing the system.

### Add Student

Add a new student record to the database.

### View Students

Display all student records in a tabular format.

### Search Students

Search students by:

* Student ID
* Name
* Department

### Update Student

Modify existing student information.

### Delete Student

Remove student records from the database.

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create the Database

Open MySQL Workbench and execute:

```sql
database.sql
```

### 4. Configure Database Credentials

Update the MySQL connection settings in `student.py`:

```python
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "YOUR_PASSWORD",
    "database": "student_management"
}
```

### 5. Run the Application

```bash
python student.py
```

### 6. Open in Browser

```text
http://127.0.0.1:5000
```

## Default Admin Credentials

```text
Username: admin
Password: admin123
```

## Learning Concepts Demonstrated

* Flask Routing
* Flask Sessions
* Form Handling
* CRUD Operations
* MySQL Database Connectivity
* SQL Queries
* HTML Templates
* Authentication Systems

## Future Improvements

* Password Hashing
* Student Profile Pictures
* Attendance Management
* Course Management
* Export Data to Excel/PDF
* Responsive User Interface
* Role-Based Access Control

## Author

Noor Fatima

