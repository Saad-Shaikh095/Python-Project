def save_data(students):
    with open("students_data.txt", "w") as file:
        for name, marks in students.items():
            file.write(f"{name} --> {marks}\n")

def load_data():
    students = {}
    try:
        with open("students_data.txt", "r") as file:
            for line in file:
                name, marks = line.strip().split(",")
                students[name] = float(marks)
    except FileNotFoundError:
        pass
    return students

def show_menu():
    print("\n<--- Student Marks Manager --->")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student Marks")
    print("4. Delete Student")
    print("5. Calculate Average Marks")
    print("6. Exit")

def student_manager():
    students = load_data()

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            name = input("Enter Student Name: ")
            marks = float(input("Enter Marks: "))
            students[name] = marks
            save_data(students)  # <-- Save after adding
            print(f"Added {name} with marks {marks}.")

        elif choice == "2":
            if not students:
                print("No students found.")
            else:
                for name, marks in students.items():
                    print(f"{name}: {marks}")

        elif choice == "3":
            name = input("Enter Student Name to Update: ")
            if name in students:
                marks = float(input("Enter New Marks: "))
                students[name] = marks
                save_data(students)  # <-- Save after updating
                print(f"Updated {name}'s marks to {marks}.")
            else:
                print("Student not found!")

        elif choice == "4":
            name = input("Enter Student Name to Delete: ")
            if name in students:
                students.pop(name)
                save_data(students)  # <-- Save after deleting
                print(f"Deleted {name}.")
            else:
                print("Student not found!")

        elif choice == "5":
            if students:
                avg = sum(students.values()) / len(students)
                print(f"Class Average Marks: {avg:.2f}")
            else:
                print("No students to calculate average.")

        elif choice == "6":
            print("Exiting Student Marks Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again!")

student_manager()
