import sqlite3
from sqlite3 import Error

def create_connection(db_file): #create database connection to SQLite db
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

'''if __name__ == '__main__': #create the db file in specified directory
    create_connection(r"/Users/arul.sethi/Desktop/db/pythonsqlite.db")'''

