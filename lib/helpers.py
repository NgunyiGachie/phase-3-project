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
    print(contact) if contact else print(
        f'Contact {name} not found')
    
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
            print(f'success: {contact}')
        except Exception as exc:
            print('Error updating contact: ', exc)
        else:
            print(f'Contact {id_} not found')

def delete_contact():
    id_ = input("Enter the contact's id: ")
    if contact := Contact.find_by_id(id_):
        contact.delete()
        print(f'Contact {id_} deleted')
    else:
        print(f'Contact {id_} not found')


#Phone Number functions
def list_phone_numbers():
    phone_numbers = PhoneNumber.get_all()
    for phone_number in phone_numbers:
        print(phone_number)

def find_phone_number_by_id():
    id_ = input("Enter the phone number's id: ")
    phone_number = PhoneNumber.find_by_id(id_)
    print(phone_number) if phone_number else print(f'Contact {id_} not found')

def find_phone_number_by_type():
    number_type = input("Enter the phone number's type: ")
    phone_number = PhoneNumber.find_by_type(number_type)
    print(phone_number) if phone_number else print(f'Phone Number {number_type} not found')

def create_phone_number():
    number = input("Enter the phone number: ")
    number_type = input("Enter the phone number type: ")
    contact_id = input("Enter the phone number's contact ID: ")
    try:
        contact_id = int(contact_id)
        phone_number = PhoneNumber.create(number=number, type=number_type, contact_id=contact_id)
        print(f'Success: {phone_number}')
    except ValueError:
        print("Error: Contact ID must be an integer.")
    except Exception as exc:
        print("Error creating a phone number:", exc)

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
        print(f'Phone Number {id_} not found')

def delete_phone_number():
    id_ = input("Enter the phone number's id: ")
    if phone_number := PhoneNumber.find_by_id(id_):
        phone_number.delete()  
        print(f'Phone number {id_} deleted')
    else:
        print(f'Phone number {id_} not found')


#email functions
def list_emails():
    emails = Email.get_all()
    for email in emails:
        print(email)

def find_emails_by_id():
    id_ = input("Enter the email id: ")  
    email = Email.find_by_id(id_)
    print(email) if email else print(f"Email {id_} not found") 

def create_email():
    email = input("Enter the contact's email: ")
    contact_id = input("Enter the contact's contact ID: ")
    try:
        contact_id = int(contact_id)
        contact_email = Email.create(email=email, contact_id=contact_id)
        print(f'Success: {contact_email}')
    except ValueError:
        print("Error: Contact ID must be an integer")
    except Exception as exc:
        print("Error creating contact:", exc)

def update_email():
    id_ = input("Enter the email's id: ")
    id_ = int(id_)
    if email := Email.find_by_id(id_):
        try:
            contact_email = input("Enter the contact's new email: ")
            email.contact_email = contact_email
            contact_id = input("Enter the email's new contact ID: ")
            email.contact_id = contact_id
            contact_id = int(contact_id)
            email.update()
            print(f'Success: {email}')
        except Exception as exc:
            print(f'Error updating email: ', exc)
    else:
        print(f'Email {id_} not found')


def delete_email():
    id_ = input("Enter the email's id: ")
    if email := Email.find_by_id(id_):
        email.delete
        print(f'Email {id_} deleted')
    else:
        print(f'Email (id_) not found')
    