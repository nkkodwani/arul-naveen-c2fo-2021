import sqlite3
from class_contact import Contact 

conn = sqlite3.connect('contacts.db')

c = conn.cursor()

#create a table for the contacts
'''c.execute("""CREATE TABLE contacts (
            first text,
            last text,
            email text,
            phone text
            )""")'''
#this table has been already been created 

cont1 = Contact('Sandy', 'Kemper', 'sandy@c2fo.com', '9135624045')
print(cont1.fullname)

#c.execute("INSERT INTO contacts VALUES ('Naveen', 'Kodwani', 'naveen@email.com', '9135624064')")
#conn.commit()

c.execute("SELECT * FROM contacts  WHERE last='Sethi' OR last='Kodwani'")
print(c.fetchall()) #fetchone prints the first row; fetchmany(n) prints n rows in a list

conn.commit()

conn.close() #good practice to close connection to db
