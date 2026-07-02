contacts = []

# add contact
def add_contact():
    while True: #used for name validation
        name = input("Enter Name: ").strip()

        if name == "":
            print("Name cannot be empty.")
        elif not name.replace(" ", "").isalpha():
            print("Name should contain only letters and spaces.")
        else:
            break

    while True: #used for mobile num validation
        mobile_number = input("Enter Mobile Number: ").strip()

        if mobile_number == "":
            print("Mobile number cannot be empty.")
        elif not mobile_number.isdigit():
            print("Mobile number must contain only digits.")
        elif len(mobile_number) != 10:
            print("Mobile number must be exactly 10 digits.")
        else:
            break

    email = input("Enter Email: ").strip()

    contact = {
        "name": name,
        "mobile_number": mobile_number,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully!")


# search contact
def search_contact():
    if len(contacts) == 0:
        print("No contacts available.")
        return

    search_name = input("Enter name to search: ").strip()

    found = False

    for contact in contacts: 
        if contact["name"].lower() == search_name.lower():
            print("\nContact Found")
            print("Name   :", contact["name"])
            print("Mobile :", contact["mobile_number"])
            print("Email  :", contact["email"])
            found = True
            break

    if not found:
        print("Contact not found.")


# update contact
def update_contact():
    if len(contacts) == 0:
        print("No contacts available.")
        return

    search_name = input("Enter name to update: ").strip()

    found = False

    for contact in contacts:
        if contact["name"].lower() == search_name.lower():

            while True:
                new_name = input("Enter New Name: ").strip()

                if new_name == "":
                    print("Name cannot be empty.")
                elif not new_name.replace(" ", "").isalpha():
                    print("Name should contain only letters.")
                else:
                    break

            while True:
                new_mobile = input("Enter New Mobile Number: ").strip()

                if not new_mobile.isdigit():
                    print("Mobile number must contain only digits.")
                elif len(new_mobile) != 10:
                    print("Mobile number must be exactly 10 digits.")
                else:
                    break

            new_email = input("Enter New Email: ").strip()

            contact["name"] = new_name
            contact["mobile_number"] = new_mobile
            contact["email"] = new_email

            print("Contact updated successfully!")
            found = True
            break

    if not found:
        print("Contact not found.")


# delete contact
def delete_contact():
    if len(contacts) == 0:
        print("No contacts available.")
        return

    search_name = input("Enter name to delete: ").strip()

    found = False

    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            found = True
            break

    if not found:
        print("Contact not found.")


# display contact
def display_contacts():
    if len(contacts) == 0:
        print("No contacts available.")
        return

    print("\n===== Contact List =====")

    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print("Name   :", contact["name"])
        print("Mobile :", contact["mobile_number"])
        print("Email  :", contact["email"])


# main manu
while True:
    print("\n===== Contact Book Menu =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        update_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        display_contacts()

    elif choice == "6":
        print("Thank you for using Contact Book.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")