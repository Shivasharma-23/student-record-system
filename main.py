import json
import os
FILE_NAME ="students.json"
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r") as file:
            return json.load(file)
    return{}
students = load_students()
def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)
def add_student():
    student_id = input("Enter student ID:").strip()
    if not student_id:
        print("Student ID cannot be empty.")
        return
    if student_id in students:
        print("Student ID already exists!")
        return
    name = input("Enter student name:").strip()
    if not name:
        print("Name cannot be empty.")
        return
    students[student_id] = name
    save_students()
    print("student added successfully!")
def view_students():
    if not students:
        print("No students found.")
        return
    for student_id, name in students.items():
        print(f"ID: {student_id}|Name: {name}")
while True:
    print("\n--- Student Record System ---")
    print("1. Add student")
    print("2. View students")
    print("3. Exit")
    choice = input("choose an option:").strip()
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalide choice!")
