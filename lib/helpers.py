from models.contacts import Contact
from models.phone_numbers import PhoneNumber
from models.emails import Email


def exit_program():
    print("Thank you for using Contact Manager")
    exit()

# Contact functions
def list_contacts():
    contacts = Contact.get_all()
    for contact in contacts:
        print(contact)

def find_contact_by_name():
    name = input("Enter the contact's name: ")
    contact = Contact.find_by_name(name)
    print(contact) if contact else print(f'Contact {name} not found')

def find_contact_by_id():
    id_ = input("Enter the contact's id: ")
    contact = Contact.find_by_id(id_)
    print(contact) if contact else print(f'Contact {id_} not found')

def create_contact():
    name = input("Enter the contact's name: ")
    address = input("Enter the contact's address: ")
    try:
        contact = Contact.create(name, address)
        print(f"Success: {contact}")
        add_phone_number_for_contact(contact)
        add_email_for_contact(contact)
    except Exception as exc:
        print("Error creating contact: ", exc)

def update_contact():
    id_ = input("Enter the contact's id: ")
    if contact := Contact.find_by_id(id_):
        try:
            name = input("Enter the contact's new name: ")
            contact.name = name
            address = input("Enter the contact's new address: ")
            contact.address = address
            contact.update()
            print(f'Success: {contact}')
            update_phone_number_for_contact(contact)
            update_email_for_contact(contact)
        except Exception as exc:
            print('Error updating contact: ', exc)
    else:
        print(f'Contact {id_} not found')

def delete_contact():
    id_ = input("Enter the contact's id: ")
    contact = Contact.find_by_id(id_)
    if contact:
        delete_contact_and_related_info(contact)
    else:
        print(f'Contact {id_} not found')

def delete_contact_and_related_info(contact):
    """Delete contact along with associated phone numbers and emails."""
    phone_numbers = contact.phone_numbers()
    for phone_number in phone_numbers:
        phone_number.delete()

    emails = contact.emails()
    for email in emails:
        email.delete()

    contact.delete()

    print(f'Contact {contact.name} and associated phone numbers and emails deleted')


# Phone Number functions
def list_phone_numbers():
    phonenumbers = PhoneNumber.get_all()
    for phone_number in phonenumbers:
        print(phone_number)

def find_phone_number_by_id():
    id_ = input("Enter the phone number's id: ")
    phone_number = PhoneNumber.find_by_id(id_)
    print(phone_number) if phone_number else print(f'Phone number {id_} not found')

def find_phone_number_by_type():
    number_type = input("Enter the phone number's type: ")
    phone_number = PhoneNumber.find_by_type(number_type)
    print(phone_number) if phone_number else print(f'Phone number {number_type} not found')

def add_phone_number_for_contact(contact):
    choice = input(f"Do you want to add a phone number for {contact.name}? (yes/no): ").lower()
    if choice == 'yes':
        number = input("Enter the phone number: ")
        number_type = input("Enter the phone number type: ")
        try:
            PhoneNumber.create(phone_number=number, number_type=number_type, contact_id=contact.id)
            print(f'Phone number added for {contact.name}')
        except Exception as exc:
            print(f'Error adding phone number: {exc}')


def update_phone_number():
    id_ = input("Enter the phone number's id: ")
    id_ = int(id_)
    if phone_number := PhoneNumber.find_by_id(id_):
        try:
            number = input("Enter the new phone number: ")
            phone_number.phone_number = number 
            number_type = input("Enter the new phone number type: ")
            phone_number.type = number_type  
            contact_id = input("Enter the phone number's new contact ID: ")
            phone_number.contact_id = int(contact_id)  
            phone_number.update()
            print(f'Success: {phone_number}')
        except Exception as exc:
            print('Error updating phone number: ', exc)
    else:
        print(f'Phone number {id_} not found')

def delete_phone_number():
    id_ = input("Enter the phone number's id: ")
    if phone_number := PhoneNumber.find_by_id(id_):
        phone_number.delete()  
        print(f'Phone number {id_} deleted')
    else:
        print(f'Phone number {id_} not found')

def update_phone_number_for_contact(contact):
    choice = input(f"Do you want to update the phone number for {contact.name}? (yes/no): ").lower()
    if choice == 'yes':
        existing_phone_numbers = contact.phone_numbers()
        if existing_phone_numbers:
            print("Existing phone numbers: ")
            for pn in existing_phone_numbers:
                print(pn)

        number = input("Enter the new phone number: ")
        number_type = input("Enter the phone number type: ")
        if existing_phone_numbers:
            phone_number = existing_phone_numbers[0]
            phone_number.phone_number = number
            phone_number.number_type = number_type
            phone_number.update()
        else:
            PhoneNumber.create(phone_number=number, number_type=number_type, contact_id=contact.id)
        print(f'Phone number updated for {contact.name}')


# Email functions
def list_emails():
    emails = Email.get_all()
    for email in emails:
        print(email)

def find_emails_by_id():
    id_ = input("Enter the email id: ")  
    email = Email.find_by_id(id_)
    print(email) if email else print(f"Email {id_} not found") 

def add_email_for_contact(contact):
    choice = input(f"Do you want to add an email for {contact.name}? (yes/no): ").lower()
    if choice == 'yes':
        email_address = input("Enter the email: ")
        try:
            Email.create(email=email_address, contact_id=contact.id)
            print(f'Email added for {contact.name}')
        except Exception as exc:
            print(f'Error adding email: {exc}')

def update_email():
    id_ = input("Enter the email's id: ")
    id_ = int(id_)
    if email := Email.find_by_id(id_):
        try:
            contact_email = input("Enter the contact's new email: ")
            email.email = contact_email
            contact_id = input("Enter the email's new contact ID: ")
            email.contact_id = int(contact_id)
            email.update()
            print(f'Success: {email}')
        except Exception as exc:
            print(f'Error updating email: ', exc)
    else:
        print(f'Email {id_} not found')

def delete_email():
    id_ = input("Enter the email's id: ")
    if email := Email.find_by_id(id_):
        email.delete()
        print(f'Email {id_} deleted')
    else:
        print(f'Email {id_} not found')

def update_email_for_contact(contact):
    choice = input(f"Do you want to update the email for {contact.name}? (yes/no): ").lower()
    if choice == 'yes':
        existing_emails = contact.emails()
        if existing_emails:
            print("Existing emails:")
            for email in existing_emails:
                print(email)
        
        email_address = input("Enter the new email: ")
        if existing_emails:
            email = existing_emails[0]
            email.email = email_address
            email.update()
        else:
            Email.create(email=email_address, contact_id=contact.id)
        print(f"Email updated for {contact.name}")
