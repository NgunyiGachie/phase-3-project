import ipdb
from models.__init__ import CONN, CURSOR
from models.contacts import Contact
from models.phone_numbers import PhoneNumber
from models.emails import Email

def setup():
    """Set up debugging environment"""
    drop_tables()
    create_tables()
    seed_data()

def drop_tables():
    """Drop all tables"""
    Contact.drop_table()
    PhoneNumber.drop_table()
    Email.drop_table()

def create_tables():
    """Create all tables"""
    Contact.create_table()
    PhoneNumber.create_table()
    Email.create_table()

def seed_data():
    """Seed the database with initial data"""
    contact1 = Contact.create("Anthony", "Nairobi")
    contact2 = Contact.create("John", "Nyahururu")
    contact3 = Contact.create("Liz", "Kasarani")
    contact4 = Contact.create("Sylvia", "Roysambu")
    contact5 = Contact.create("Ruth", "Juja")
    contact6 = Contact.create("Kennedy", "Seasons")

    PhoneNumber.create("0728661476", "Personal", contact1.id)
    PhoneNumber.create("0721983254", "Home", contact2.id)
    PhoneNumber.create("0707641726", "Personal", contact3.id)
    PhoneNumber.create("0746563187", "Home", contact4.id)
    PhoneNumber.create("0795159614", "Home", contact5.id)
    PhoneNumber.create("0797942162", "Personal", contact6.id)

    Email.create("antogachie@gmail.com", contact1.id)
    Email.create("john@gamail.com", contact2.id)
    Email.create("yvettelizk@gmail.com", contact3.id)
    Email.create("sylviahngunyi@gmail.com", contact4.id)
    Email.create("ruthgath015@gmail.com", contact5.id)
    Email.create("kennyngunyi@gmail.com", contact6.id)

def main():
    """Main function to run the debug tests"""
    setup()
    ipdb.set_trace()


if __name__ == "__main__":
    main()