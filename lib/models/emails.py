from init import CURSOR, CONN
from contacts import Contact

class Email:
    
    all = {}

    def __init__(self, email, contact_id, id=None):
        self.id = id
        self.email = email
        self.contact_id = contact_id

    def __repr__(self):
        return (
            f"<Email {self.id}: {self.email}, Contact ID: {self.contact_id}>"
        )
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        if not isinstance(email, str) or not email:
            raise ValueError("Email must be a non-empty string")
        self._email = email

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
        """Create a new table to persist the attributes of the Email instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY,
            email TEXT,
            contact_id INTEGER,
            FOREIGN KEY (contact_id) REFERENCES contacts(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists the Email instances"""
        sql = """
            DROP TABLE IF EXISTS emails;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the email and contact_id of the current Email object. Update object id attribute using the primary key value of new row. Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO emails (email, contact_id)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.email, self.contact_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Email instance"""
        sql = """
            UPDATE emails
            SET email = ?, contact_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.email, self.contact_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Email instance, delete the dictionary entry, and reassign the id attribute"""
        sql = """
            DELETE FROM emails
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, email, contact_id):
        """Initialize a new Email instance and save the object to the database"""
        email = cls(email, contact_id)
        email.save()
        return email

    @classmethod
    def instance_from_db(cls, row):
        """Return an Email object having the attribute values of the table row"""
        email = cls.all.get(row[0])
        if email:
            email.email = row[1]
            email.contact_id = row[2]
        else:
            email = cls(row[1], row[2], row[0])
            email.id = row[0]
            cls.all[email.id] = email
        return email
        
    @classmethod
    def get_all(cls):
        """Return a list containing one Email object per table row"""
        sql = """
            SELECT *
            FROM emails
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return Email object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM emails
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
