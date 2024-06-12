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
    pass


def create_tables():
    pass

def seed_data():
    pass