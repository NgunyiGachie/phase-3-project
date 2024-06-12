import sqlite3

CONN = sqlite3.connect('contact_manager.db')
CURSOR = CONN.cursor()