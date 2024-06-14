# Contact Manager

## Overview
This project is a Contact Management System that allows users to manage contacts, their email addresses, and phone numbers. It provides functionalities to create, read, update, and delete (CRUD) contacts, emails, and phone numbers. The project uses SQLite as the database and follows object-oriented programming (ORM) principles.

## Features

- **Contact Management**
  - Create new contacts
  - List all contacts
  - Find contact by ID
  - Update contact details
  - Delete contacts

- **Email Management**
  - Add email addresses to contacts
  - List all email addresses
  - Find email by ID
  - Update email details
  - Delete email addresses

- **Phone Number Management**
  - Add phone numbers to contacts
  - List all phone numbers
  - Find phone number by ID
  - Update phone number details
  - Delete phone numbers

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/phase-3-project.git
    cd phase-3-project
    ```

2. **Install the required dependencies:**
    ```sh
    pipenv install
    ```

3. **Set up a virtual environment:**
    ```sh
    pipenv shell
    ```

4. **Set up the database:**
    ```python
    from models.contacts import Contact
    from models.emails import Email
    from models.phone_numbers import PhoneNumber

    Contact.create_table()
    Email.create_table()
    PhoneNumber.create_table()

## Usage

### Running the CLI

To run the command line interface (CLI), you need to make the `cli.py` script executable and then execute it:

1. **Make the script executable:**
    ```sh
    chmod +x lib/cli.py
    ```

2. **Run the script directly:**
    ```sh
    ./lib/cli.py
    ```

Alternatively, you can still run the script with Python:
```sh
python lib/cli.py



