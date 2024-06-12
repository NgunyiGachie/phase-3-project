from models.__init__ import CURSOR, CONN
from models.contacts import Contact

class PhoneNumber: 
    
    all = {}

    def __init__(self, phone_number, type, contact_id, id=None):
        self.id = id
        self.contact_id = contact_id
        self.phone_number = phone_number
        self.type = type
    
    def __repr__(self):
        return (
            f"<PhoneNumber {self.id}: {self.phone_number}, {self.type}," +
            f"Contact ID: {self.contact_id}>"
        )
    
    @property
    def phone_number(self):
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, phone_number):
        if not isinstance(phone_number, str) or not phone_number:
            raise ValueError("Phone Number must be a non-empty string.")
        self._phone_number = phone_number

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        if not isinstance(type, str) or not type:
            raise ValueError("Type must be a non-empty string.")
        self._type = type

    @property
    def contact_id(self):
        return self._contact_id
    
    @contact_id.setter
    def contact_id(self, contact_id):
        if isinstance(contact_id, int) and Contact.find_by_id(contact_id):
            self._contact_id = contact_id
        else:
            raise ValueError("contact_id must reference a contact in the database")
        
    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of PhoneNumber instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS phonenumbers (
            id INTEGER PRIMARY KEY,
            phone_number TEXT,
            type TEXT,
            contact_id INTEGER,
            FOREIGN KEY (contact_id) REFERENCES contacts(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists PhoneNumber instances"""
        sql = """
            DROP TABLE IF EXISTS phonenumbers
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with phone number, type, and contact id values of the current PhoneNumber object. Update object id attribute using the primary key of new row. Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO phonenumbers (phone_number, type, contact_id)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.phone_number, self.type, self.contact_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current PhoneNumber instance."""
        sql = """
            UPDATE phonenumbers
            SET phone_number = ?, type = ?, contact_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.phone_number, self.type, self.contact_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current PhoneNumber instance, delete the dictionary entry, and reassign id attribute"""
        sql = """
            DELETE FROM phonenumbers
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, phone_number, type, contact_id):
        """Initialize a new PhoneNumber instance and save the object to the database"""
        phone_number = cls(phone_number, type, contact_id)
        phone_number.save()
        return phone_number
    
    @classmethod
    def instance_from_db(cls, row):
        """Return a PhoneNumber object having the attribute values from the table row"""
        phone_number = cls.all.get(row[0])
        if phone_number:
            phone_number.phone_number = row[1]
            phone_number.type = row[2]
            phone_number.contact_id = row[3]
        else:
            phone_number = cls(row[1], row[2], row[3])
            phone_number.id = row[0]
            cls.all[phone_number.id] = phone_number
        return phone_number
    
    @classmethod
    def get_all(cls):
        """Return a list containing one PhoneNumber object per table row"""
        sql = """
            SELECT *
            FROM phonenumbers
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return PhoneNumber object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM phonenumbers
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_type(cls, type):
        """Return PhoneNumber object corresponding to the first table row matching specified type"""
        sql = """
            SELECT *
            FROM phonenumbers
            WHERE type = ?
        """
        row = CURSOR.execute(sql, (type,)).fetchone()
        return cls.instance_from_db(row) if row else None
