# Student Management System

A Django-based Student Management System developed as a Full Stack Web Developer Assessment Project.

## Features

- User Authentication (Login / Logout)
- Dashboard
- Student Management (CRUD)
- Course Management (CRUD)
- Faculty Management (CRUD)
- Faculty-wise Assigned Courses
- Attendance Management
- Student Search
- Export Students to Excel
- Export Students to PDF
- Bulk Student Import (CSV)
- Audit Log

## Technologies Used

- Python 3
- Django
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- SQLite3
- OpenPyXL
- ReportLab

## Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Create virtual environment

```bash
python -m venv .venv
```

3. Activate virtual environment

```bash
.venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Apply migrations

```bash
python manage.py migrate
```

6. Run the project

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

## Modules

- Dashboard
- Students
- Courses
- Faculty
- Attendance
- Audit Log

## Database

SQLite3

## Developed By

Sania Thahaseen