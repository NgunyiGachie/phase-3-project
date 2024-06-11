from _init_ import CURSOR, CONN 

class Contact: 
    
    all = {}
    
    def __init__(self, name, address):
        self.id = id
        self.name = name
        self.address = address

    def _repr_(self):
        return f"<Contact {self.id}: {self.name}, {self.address}, {self.birthday}>"
    
    @property
    def name(self):
        return self.__qualname__
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string")
        self._name = name

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, address):
        if not isinstance(address, str) or not address:
            raise ValueError("Address must be a non-empty string")
        self._address = address

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Contact instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS contacts(
            id INTEGER PRIMARY KEY,
            name TEXT
            address TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Contact instances"""
        sql = """
            Drop TABLE IF EXISTS contacts;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and address values of the current Contact instance. Update object id attribute using the primary key value of new row. Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO contacts (name, address)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.address))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, address):
        """ Initialize a new Contact instance and save the object in the database"""
        contact = cls(name, address)
        contact.save()
        return contact
    
    def update(self):
        """Update the table row corresponding to the current Contact instance."""
        sql = """
            UPDATE contacts
            SET name = ?, address = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.address, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Contact instance, delete the dictionary entry, and reassign id attribute"""
        sql = """
            DELETE FROM contacts
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Contact object having the attribute values from the table row."""
        contact = cls.all.get(row[0])
        if contact:
            contact.name = row[1]
            contact.address = row[2]
        else:
            contact = cls(row[1], row[2])
            contact.id = row[0]
            cls.all[contact.id] = contact
        return contact
    
    @classmethod
    def get_all(cls):
        """Return a list containing a Contact object per row in the table."""
        sql= """
            SELECT *
            FROM contacts
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, self):
        """Return a Contact object corresponding to the table row matching the specified primary key."""
        sql = """
            SELECT *
            FROM contacts
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """Return a Contact object corresponding to the first table row matching specified name"""
        sql = """
            SELECT *
            FROM contacts
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def phone_numbers(self):
        """Return list of phone numbers with current contact"""
        from phone_numbers import PhoneNumber
        sql = """
            SELECT * FROM phone_numbers
            WHERE contact_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [PhoneNumber.instance_from_db(row) for row in rows]
        
    