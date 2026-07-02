students_management = {} #dictionary to store student data

def addstudent():  #add student
    while True:
        try:
            stud_id = int(input("Enter Student ID: "))
            break
        except ValueError:
            print("Please enter a valid numeric Student ID.")

    while True:
        name = input("Enter Student Name: ") #take input from user for student name

        if name.strip() == "": #if name is empty, print error message
            print("Name cannot be empty.")

        elif not name.replace(" ", "").isalpha(): 
            print("Name should contain only letters.")

        else:
            break



    while True:
        try:
            marks = float(input("Enter Student Marks: "))
            break
        except ValueError:
            print("Invalid Input! Please enter marks in numbers.")

    students_management[stud_id] = {
        "name": name, 
        "marks": marks
    }

    print("Student added successfully.")

def updatestudent(): #upadte student
    stud_id = int(input("Enter Student ID: "))

    if stud_id in students_management:

        while True:
            name = input("Enter Student Name: ")

            if name.strip() == "":
                print("Name cannot be empty.")

            elif not name.replace(" ", "").isalpha():
                print("Name should contain only letters.")

            else:
                break

        while True:
            try:
                marks = float(input("Enter New Marks: "))
                break
            except ValueError:
                print("Invalid Input! Please enter marks in numbers.")

        students_management[stud_id]["name"] = name 
        students_management[stud_id]["marks"] = marks

        print("Student updated successfully")

    else:
        print("Student not found")

def deletestudent(): #delete student
    stud_id=int(input("Enter Student id :"))
    if stud_id in students_management:
        del students_management[stud_id] #delete student from dictionary
        print("Student deleted successfully")
    else:
        print("Student not found")

def searchstudent(): #search student
    stud_id=int(input("Enter student id :"))
    if stud_id in students_management:
        print("Student id :",stud_id)
        print("Student name :",students_management[stud_id]["name"])
        print("Student marks :",students_management[stud_id]["marks"])
    else:
        print("student not found")

def displaystudent(): #display student
    if len(students_management) == 0: #find any student in dictionary or not
        print("No students found")
    else:
        for stud_id, student in students_management.items(): 
            print("\n--------------------")
            print("Student id :",stud_id)
            print("Student name :",student["name"])
            print("Student marks :",student["marks"])

def avgmarks(): #average marks
    if len(students_management) == 0:
        print("No students found")
    else:
        total = 0

        for student_id in students_management:
            total += students_management[student_id]["marks"] #take marks from dictionary and add to total

        average = total / len(students_management) #calculate average marks

        print("Average Marks :", average)

def topperstudent(): #topper student
    if len(students_management) == 0:
        print("Student not found")
        return

    highest_marks = -1 #intilialize because marks cant be negative
    topper_id = ""

    for stud_id in students_management:
        if students_management[stud_id]["marks"] > highest_marks: #store highest marks and student id of topper student
            highest_marks = students_management[stud_id]["marks"] #if new student enter with higher marks 
            topper_id = stud_id

    print("Topper Student ID :", topper_id)
    print("Topper Student Name :", students_management[topper_id]["name"])
    print("Topper Student Marks :", students_management[topper_id]["marks"])
            
while True: #main block of the code
    print("\nStudent Management System")

    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Display Students")
    print("6. Average Marks")
    print("7. Topper Student")
    print("8. Exit")

    choice = input("Enter Your Choice (1-8): ")

    if not choice.isdigit(): #check if input is a number or not
        print("Please enter numbers only.")
        continue

    if choice == "1":
        addstudent()

    elif choice == "2":
        updatestudent()

    elif choice == "3":
        deletestudent()

    elif choice == "4":
        searchstudent()

    elif choice == "5":
        displaystudent()

    elif choice == "6":
        avgmarks()

    elif choice == "7":
        topperstudent()

    elif choice == "8":
        print("Exiting...")
        break

    else:
        print("Invalid Choice.")