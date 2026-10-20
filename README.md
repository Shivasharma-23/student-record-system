# Student Record Management System

A beginner-friendly command-line application built with Python to manage student records using JSON file storage.

## Features

- Add new student records
- View all students
- Search students by student ID
- Update student details
- Delete student records with confirmation
- Validate empty inputs and duplicate student IDs
- Store student records in a JSON file
- Handle storage errors safely
- Log application events and errors
- Automated tests using Python's `unittest` framework

## Technologies Used

- **Python 3**
- **JSON** for data persistence
- **unittest** for automated testing
- **unittest.mock** for simulating user input and storage failures
- **Git and GitHub** for version control

## Requirements

- Python 3 installed
- Git (optional, for cloning the repository)

No third-party Python packages are required.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Shivasharma-23/student-record-system.git
```

### 2. Open the project folder

```bash
cd student-record-system
```

### 3. Run the application

```bash
python main.py
```

### 4. Run the automated tests

```bash
python -m unittest discover -v
```

## Data Storage

Student records are stored locally in `students.json`. The application loads saved records when it starts and saves changes when student records are modified.

The `students.json` file is excluded from Git so that local student data is not uploaded to the repository.

## Project Structure

```text
student-record-system/
├── main.py
├── student_manager.py
├── students.json
├── test_main.py
├── test_load_students.py
├── test_basic.py
├── README.md
└── .gitignore
```

## Learning Outcomes

This project demonstrates practical experience with:

- Python functions and dictionaries
- CRUD operations (Create, Read, Update, Delete)
- JSON file handling
- Input validation and exception handling
- Logging
- Automated unit testing
- Git branching, commits, and GitHub

## Future Improvements

- Add a graphical user interface
- Replace JSON storage with SQLite
- Add more validation and automated tests

## Author

**Shiva Sharma**


## Demo

The Student Record Management System runs in the terminal and supports:

- Adding student records
- Viewing saved students
- Searching by student ID
- Updating student details
- Deleting records with confirmation

Run the application using:

```bash
python main.py
```

## Example Output

```text
--- Student Record System ---
1. Add student
2. View students
3. Search Student
4. Update student
5. Delete student
6. Exit

ID: 101 | Name: Monkey D Luffy
ID: 102 | Name: Naruto
ID: 103 | Name: Zoro
```
