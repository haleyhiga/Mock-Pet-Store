import os
import sys
import sqlite3

PET_STORE_NAME = "PetHouse"
DB_FILE = PET_STORE_NAME + ".db"

def getDatabase(create=False):
    if os.path.exists(DB_FILE):
        if create:
            os.remove(DB_FILE)
    else:
        if not create:
            print("getDatabase: No database has been discovered.")
            sys.exit(1)
    
    con = sqlite3.connect(DB_FILE)
    con.execute('PRAGMA foreign_keys = ON')
    return con

def deleteDatabase():
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
        print("deleteDatabase: Database has been deleted.")
    else:
        print("deleteDatabase: No database exists.")
        sys.exit(1)

def createDatabase():
    with getDatabase(create = True) as con:

        # Type of Pets
        con.execute('''
CREATE TABLE pet_types (
    id                 INTEGER PRIMARY KEY,
    type               TEXT NOT NULL,
    breed              TEXT NOT NULL UNIQUE
)
''')
        # Type of Appts & Services
        con.execute('''
CREATE TABLE service_types (
    id                  INTEGER PRIMARY KEY,
    type                TEXT NOT NULL UNIQUE,
    plan                TEXT NOT NULL,
    description         TEXT,
    price               INTEGER
)
''')
        # Type of Products
        con.execute('''
CREATE TABLE product_types (
    id                  INTEGER PRIMARY KEY,
    type                TEXT NOT NULL UNIQUE,
    pet_type_id         INTEGER NOT NULL,
    description         TEXT,
    FOREIGN KEY(pet_type_id) REFERENCES pet_types(id) ON DELETE CASCADE ON UPDATE CASCADE
)
''')

        # Employee Depts
        con.execute('''
CREATE TABLE employee_departments (
    id                  INTEGER PRIMARY KEY,
    type                TEXT NOT NULL UNIQUE,
    description         TEXT
)
''')
        # Coupons / Deals
        con.execute('''
CREATE TABLE coupons (
    id                  INTEGER PRIMARY KEY,
    name                TEXT NOT NULL UNIQUE,
    type_of_discount    TEXT,
    start_valid_date    INTEGER,
    end_valid_date      INTEGER,
    constraints         TEXT
)
''')
        # Products
        con.execute('''
CREATE TABLE products (
    id                  INTEGER PRIMARY KEY,
    name                TEXT NOT NULL UNIQUE,
    product_type_id     INTEGER NOT NULL,
    pet_type_id         INTEGER NOT NULL,
    stock               INTEGER,
    price               INTEGER,
    FOREIGN KEY(product_type_id) REFERENCES product_types(id) ON DELETE CASCADE ON UPDATE CASCADE
    FOREIGN KEY(pet_type_id) REFERENCES pet_types(id) ON DELETE CASCADE ON UPDATE CASCADE
)
''')

        # Adoptions
        con.execute('''
CREATE TABLE adoptions (
    id                  INTEGER PRIMARY KEY,
    pet_type_id         INTEGER,
    price               INTEGER,
    available           BOOLEAN NOT NULL,
    age                 INTEGER,
    description         TEXT,
    FOREIGN KEY(pet_type_id) REFERENCES pet_types(id) ON DELETE CASCADE ON UPDATE CASCADE
)
''')

        # Employees
        con.execute('''
CREATE TABLE employees (
    id                  INTEGER PRIMARY KEY,
    dept_id             INTEGER,
    name                TEXT UNIQUE,
    shifts              TEXT,
    FOREIGN KEY(dept_id) REFERENCES employee_departments(id) ON DELETE CASCADE ON UPDATE CASCADE
)
''')

        # Employee Schedules
        con.execute('''
CREATE TABLE employee_schedules (
    id                  INTEGER PRIMARY KEY,               
    employee_id         INTEGER,
    starting_time       INTEGER,
    ending_time         INTEGER,
    FOREIGN KEY(employee_id) REFERENCES employees(id) ON DELETE CASCADE ON UPDATE CASCADE
)
''')

        # Customers
        con.execute('''
CREATE TABLE customers (
    id                    INTEGER PRIMARY KEY,
    name                  TEXT NOT NULL UNIQUE,
    email                 TEXT NOT NULL,
    phone_number          TEXT NOT NULL,
    pet_id                INTEGER,
    FOREIGN KEY(pet_id) REFERENCES pets(id) ON DELETE CASCADE ON UPDATE CASCADE
)
''')

        # Pets
        con.execute('''
CREATE TABLE pets (
    id                    INTEGER PRIMARY KEY,
    customer_id           TEXT,
    pet_type_id           TEXT,
    pet_name              TEXT,
    age                   INTEGER,  
    FOREIGN KEY(pet_type_id) REFERENCES pet_types(id) ON DELETE CASCADE ON UPDATE CASCADE
)
''')

        # Appts (Schedules)
        con.execute('''
CREATE TABLE services_schedule (
    id                    INTEGER PRIMARY KEY,
    service_type_id       INTEGER,
    pet_id                INTEGER,
    customer_id           INTEGER,
    start_time            INTEGER,  
    end_time              INTEGER, 
    FOREIGN KEY(pet_id) REFERENCES pets(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(service_type_id) REFERENCES service_types(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(customer_id) REFERENCES customers(id) ON DELETE CASCADE ON UPDATE CASCADE
)
''')


        # Subscriptions / Memberships
        con.execute('''
CREATE TABLE memberships (
    id                    INTEGER PRIMARY KEY,
    customer_id           INTEGER NOT NULL UNIQUE,
    active                BOOL,
    years_subscribed      INTEGER,
    FOREIGN KEY(customer_id) REFERENCES customers(id) ON DELETE CASCADE ON UPDATE CASCADE
)
''')


        # Rooms
        con.execute('''
CREATE TABLE rooms (
    id                    INTEGER PRIMARY KEY,
    service_type_id       INTEGER,
    employee_dept_id      INTEGER,
    name                  TEXT NOT NULL,
    description           TEXT,
    FOREIGN KEY(employee_dept_id) REFERENCES employee_departments(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(service_type_id) REFERENCES service_types(id) ON DELETE CASCADE ON UPDATE CASCADE
)
''')




    print("createDatabase: Database has been successfully created.")
    con.commit()