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
def search_student():
    student_id = input("Enter student ID To search: ").strip()
    if student_id in students:
        print("Student found!")
        print(f"ID: {student_id} | Name: {students[student_id]}")
    else:
        print("Student not found.")
def update_student():
    student_id = input("Enter student ID to update:").strip()
    if student_id in students:
        new_name = input("Enter new student name:").strip()
        if not new_name:
            print("Name cannot be empty.")
            return
        students[student_id] = new_name
        save_students()
        print("Student Updated successfully!")
    else:
        print("Student not found.")
def delete_student():
    student_id = input("Enter student ID to delete:").strip()
    if student_id in students:
        confirm = input(f"Are you sure you want to delete student {students[student_id]}? (yes/no):").strip().lower()
        if confirm == "yes":
            del students[student_id]
            save_students()
            print("Student deleted successfully!")
        else:
            print("Deletion cancelled.")
    else:
        print("Student not found.")
def main():
    while True:
        print("\n--- Student Record System ---")
        print("1. Add student")
        print("2. View students")
        print("3. Search Student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Exit")
        choice = input("choose an option:").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
        pass
if __name__ == "__main__":
    main()