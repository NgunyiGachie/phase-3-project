from helpers import (
    exit_program,
    list_contacts,
    find_contact_by_name,
    find_contact_by_id,
    create_contact,
    update_contact,
    delete_contact,
    list_phone_numbers,
    find_phone_number_by_id,
    find_phone_number_by_type,
    update_phone_number,
    delete_phone_number,
    list_emails,
    find_emails_by_id,
    update_email,
    delete_email
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_contacts()
        elif choice == "2":
            find_contact_by_name()
        elif choice == "3":
            find_contact_by_id()
        elif choice == "4":
            create_contact()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            delete_contact()
        elif choice == "7":
            list_phone_numbers()
        elif choice == "8":
            find_phone_number_by_id()
        elif choice == "9":
            find_phone_number_by_type()
        elif choice == "10":
            update_phone_number()
        elif choice == "11":
            delete_phone_number()
        elif choice == "12":
            list_emails()
        elif choice == "13":
            find_emails_by_id()
        elif choice == "14":
            update_email()
        elif choice == "15":
            delete_email()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all contacts")
    print("2. Find contact by name")
    print("3. Find contact by id")
    print("4. Create a contact")
    print("5. Update contact")
    print("6. Delete a contact")
    print("7. List all phone numbers")
    print("8. Find phone numbers by id")
    print("9. Find phone number by type")
    print("10. Update phone number")
    print("11. Delete phone number")
    print("12. List all emails")
    print("13. Find emails by id")
    print("14. Update an email")
    print("15. Delete an email")

if __name__ == '__main__':
    main()