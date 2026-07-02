
# File name
file_name = "students.txt"


# Function to add student record
def add_student():

    # Validate Student ID
    while True:
        student_id = input("Enter Student ID: ").strip()

        if student_id == "":
            print("Student ID cannot be empty.")
        elif not student_id.isdigit():
            print("Student ID should contain only digits.")
        else:
            break

    # Validate Student Name
    while True:
        student_name = input("Enter Student Name: ").strip()

        if student_name == "":
            print("Student Name cannot be empty.")
        elif not student_name.replace(" ", "").isalpha():
            print("Student Name should contain only letters and spaces.")
        else:
            break

    # Validate Course
    while True:
        course = input("Enter Course Name: ").strip()

        if course == "":
            print("Course Name cannot be empty.")
        else:
            break

    # Open file in append mode
    file = open(file_name, "a")

    # Store student information
    file.write(student_id + "," + student_name + "," + course + "\n")

    # Close file
    file.close()

    print("Student Record Added Successfully.")


# Function to display all student records
def display_students():

    try:

        # Open file in read mode
        file = open(file_name, "r")

        # Read all records
        records = file.readlines()

        # Close file
        file.close()

        # Check if file is empty
        if len(records) == 0:
            print("No student records found.")
            return

        print("\n----- Student Records -----")

        # Display each record
        for record in records:

            data = record.strip().split(",")

            print("Student ID   :", data[0])
            print("Student Name :", data[1])
            print("Course       :", data[2])
            print("---------------------------")

    except FileNotFoundError:
        print("No student records found.")


# Main Menu
while True:

    print("\n===== Student File Handling System =====")
    print("1. Add Student Record")
    print("2. Display Student Records")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    # Add Student Record
    if choice == "1":
        add_student()

    # Display Student Records
    elif choice == "2":
        display_students()

    # Exit Program
    elif choice == "3":
        print("Thank you for using Student File Handling System.")
        break

    # Invalid Choice
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
