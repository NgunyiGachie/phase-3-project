from models.__init__ import CURSOR, CONN
from models.contacts import Contact
from models.phone_numbers import PhoneNumber
from models.emails import Email

def create_tables():
    Contact.create_table()
    PhoneNumber.create_table()
    Email.create_table()

def drop_tables():
    Contact.drop_table()
    PhoneNumber.drop_table()
    Email.drop_table()

def seed_data():
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

if __name__ == '__main__':
    drop_tables()
    create_tables()
    seed_data()  
    CONN.close()
