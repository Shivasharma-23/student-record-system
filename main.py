students = {}
def add_student():
    student_id = input("Enter student ID:")
    name = input("Enter the student name:")
    students[student_id] = name
    print("student added successfully!")
def view_students():
    if not students:
        print("No student found.")
        return
    for student_id, name in students.items():
        print(f"ID:{student_id}| Name:{name}")
while True:
    print("\n1. add student")
    print("2. view student")
    print("3. exit")
    choice = input("choose an option: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
