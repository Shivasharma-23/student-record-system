import student_manager
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s")
logging.info("Student added successfully")
logging.warning("Student ID already exists")
logging.error("Unable to save student data")
FILE_NAME = student_manager.FILE_NAME
students = student_manager.load_students()
def add_student():
    student_id = input("Enter student ID:").strip()
    if not student_id:
        print("Student ID cannot be empty.")
        return
    if student_id in students:
        logging.warning("Student ID already exists")
        return
    name = input("Enter student name:").strip()
    if not name:
        print("Name cannot be empty.")
        return
    students[student_id] = name

    try:
        student_manager.save_students(students)
    except (OSError, ValueError) as error:
        del students[student_id]
        logging.error("Unable to save student data: %s", error)
        print("Unable to save student data.")
        return
    logging.info("Student added successfully")

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
        student_manager.save_students(students)
        logging.info("Student updated successfully!")
    else:
        print("Student not found.")
def delete_student():
    student_id = input("Enter student ID to delete:").strip()
    if student_id in students:
        confirm = input(f"Are you sure you want to delete student {students[student_id]}? (yes/no):").strip().lower()
        if confirm == "yes":
            del students[student_id]
            student_manager.save_students(students)
            logging.info("Student deleted successfully!")
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