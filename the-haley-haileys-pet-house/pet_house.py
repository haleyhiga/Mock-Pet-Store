import db
import os

class PetHouse:
    def __init__(self, create):
        self.mTables = []

        if create:
            con = db.getDatabase()
            cur = con.cursor()

            tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = tables.fetchall()

            if len(tables) != 0:
                for table in tables:
                    self.mTables.append(table[0])
            else:
                print("PetHouse: error: There are no tables in the database.")
            con.close()
    
    # DATABASE MANAGEMENT
    def getTables(self):
        return self.mTables
    
    def deleteDatabase(self):
        db.deleteDatabase()
        
    def createDatabase(self):
        db.createDatabase()

    # PET TYPES
    def getAllPetTypes(self):
        con = db.getDatabase()
        cur = con.cursor()

        pets = cur.execute("SELECT type, breed FROM pet_types")
        pets = pets.fetchall()

        if len(pets) == 0:
            print("There are currently no pet types.")
            con.close()
            return

        d = {}
        for pet in pets:
            type = pet[0]
            breed = pet[1]

            if type in d:
                d[type].append(breed)
            else:
                d[type] = [breed]

        print("Pet Types:")
        for type in d:
            print(type+":")
            for breed in d[type]:
                print("\t"+breed)
        
        con.close()

    def getPetType(self, type):
        con = db.getDatabase()
        cur = con.cursor()

        pet_type = cur.execute("SELECT * FROM pet_types WHERE type=?", (type,))
        pet_type = pet_type.fetchall()

        if len(pet_type) == 0:
            print(type, "does not exist.")
            con.close()
            return

        print(type,"has these breeds:")
        for (id, _, breed) in pet_type:
            print("\t"+str(id)+":",breed)

        con.close()

    def addPetType(self, type, breed):
        # Type: TEXT NOT NULL UNIQUE
        # Breed: TEXT NOT NULL UNIQUE
        
        con = db.getDatabase()
        cur = con.cursor()

        cur.execute("INSERT INTO pet_types (type, breed) VALUES(?, ?)", (type, breed,))
        print(type,"with breed", breed,"was added to the database.")

        con.commit()
        con.close()

    def deletePetType(self, type):
        # Type: TEXT NOT NULL UNIQUE

        con = db.getDatabase()
        cur = con.cursor()

        pet = cur.execute("SELECT id FROM pet_types WHERE type = ?", (type,))
        pet = pet.fetchall()

        if len(pet) == 0:
            print(type, "does not exist in the database.")
            con.close()
            return
        
        for (id,) in pet:
            cur.execute("DELETE FROM pet_types WHERE id = ?", (id,))
        print(type, "was successfully deleted from the database.")

        con.commit()
        con.close()

    # SERVICE TYPES
    def getAllServiceTypes(self):
        con = db.getDatabase()
        cur = con.cursor()

        services = cur.execute("SELECT type FROM service_types")
        services = services.fetchall()

        for (service,) in services:
            print(service)
        
        con.close()

    def getServiceType(self, type):
        # Type: TEXT NOT NULL UNIQUE
        
        con = db.getDatabase()
        cur = con.cursor()

        services = cur.execute("SELECT * FROM service_types")
        services = services.fetchall()

        if len(services) == 0:
            print("There are currently no service types.")
            con.close()
            return

        print("Service Types:")
        for (id, type, plan, description, price) in services:
            print("\t",id, type, plan, description, price)
        
        con.close()
    
    def addServiceType(self, type, plan, description, price):
        # Type: TEXT NOT NULL UNIQUE
        # Plan: TEXT NOT NULL
        # Description: TEXT
        # Price: INTEGER
        
        con = db.getDatabase()
        cur = con.cursor()

        cur.execute("INSERT INTO service_types (type, plan, description, price) VALUES(?, ?, ?, ?)", (type, plan, description, price,))
        print(type,"service with", plan,"was added to the database.")
        print("\tDescription:", description)
        print("\tPrice:", price)

        con.commit()
        con.close()

    def deleteServiceType(self, type):
        # Type: TEXT NOT NULL UNIQUE
        con = db.getDatabase()
        cur = con.cursor()

        service = cur.execute("SELECT id FROM service_types WHERE type = ?", (type,))
        service = service.fetchall()


        if len(service) == 0:
            print(type, "does not exist in the database.")
            con.close()
            return
        
        for (id,) in service:
            cur.execute("DELETE FROM service_types WHERE id = ?", (id,))
        print(type, "was successfully deleted from the database.")
        
        con.commit()
        con.close()

    # PRODUCT TYPES
    def getAllProductTypes(self):
        con = db.getDatabase()
        cur = con.cursor()

        
        con.close()

    def getProductType(self, type):
        # Type: TEXT NOT NULL UNIQUE

        con = db.getDatabase()
        cur = con.cursor()

        
        con.close()
    
    def addProductType(self, type, description):
        # Type: TEXT NOT NULL UNIQUE
        # Description: TEXT
        
        con = db.getDatabase()
        cur = con.cursor()

        cur.execute("INSERT INTO product_types (type, description) VALUES(?, ?)", (type, description,))
        print(type,"product type was added to the database.")
        print("\tDescription:", description)

        
        con.commit()
        con.close()
    
    def deleteProductType(self, type):
        # Type: TEXT NOT NULL UNIQUE
        
        con = db.getDatabase()
        cur = con.cursor()

        
        con.commit()
        con.close()
    
    # EMPLOYEE DEPARTMENTS  
    def getAllEmployeeDepartments(self):
        
        con = db.getDatabase()
        cur = con.cursor()

        
        con.close()

    def getEmployeeDepartment(self, type):
        # Type: TEXT NOT NULL UNIQUE

        con = db.getDatabase()
        cur = con.cursor()

        
        con.close()
    
    def addEmployeeDepartment(self, type, description):
        # Type: TEXT NOT NULL UNIQUE
        # Description: TEXT
        
        con = db.getDatabase()
        cur = con.cursor()

        cur.execute("INSERT INTO employee_departments (type, description) VALUES(?, ?)", (type, description,))
        print(type,"employee department was added to the database.")
        print("\tDescription:", description)
        
        con.commit()
        con.close()

    def deleteEmployeeDepartment(self, type):
        # Type: TEXT NOT NULL UNIQUE
        
        con = db.getDatabase()
        cur = con.cursor()

        
        con.commit()
        con.close()
        
    # COUPONS
    def getAllCoupons(self):
        con = db.getDatabase()
        cur = con.cursor()

        
        con.close()

    def getCoupon(self, name):
        # Name: TEXT NOT NULL UNIQUE
        
        con = db.getDatabase()
        cur = con.cursor()

        
        con.close()

    def addCoupon(self, name, type, start, end, constraints):
        # Name: TEXT NOT NULL UNIQUE
        # Type: TEXT
        # Start: INTEGER
        # End: INTEGER
        # Constraints: TEXT
        
        con = db.getDatabase()
        cur = con.cursor()

        cur.execute("INSERT INTO coupons (name, type, start, end, constraints) VALUES(?, ?, ?, ?, ?)", (name, type, start, end, constraints))
        print(name,"coupon was added to the database.")
        print("\tType:", type)
        print("\tStart:", start)
        print("\tEnd:", end)
        print("\tContraints:", constraints)

        

        
        con.commit()
        con.close()
    
    def deleteCoupon(self, name):
        # Name: TEXT NOT NULL UNIQUE
        
        con = db.getDatabase()
        cur = con.cursor()

        
        con.commit()
        con.close()

    # PRODUCTS
    def getAllProducts(self):
        
        con = db.getDatabase()
        cur = con.cursor()



        
        con.close()

    def getProduct(self, name):
        # Name: TEXT NOT NULL UNIQUE
        
        con = db.getDatabase()
        cur = con.cursor()

        
        con.close()

    def addProduct(self, name, product_type, pet_type, stock, price):
        # Name: TEXT NOT NULL UNIQUE
        # Product Type: TEXT
        # Pet_type: TEXT
        # Stock: INTEGER
        # Price: INTEGER

        con = db.getDatabase()
        cur = con.cursor()

        product_type_id = cur.execute("SELECT id FROM product_types WHERE type = ?", product_type)
        product_type_id = product_type_id.fetchall()
        pet_type_id = cur.execute("SELECT id FROM pet_types WHERE type = ?", pet_type)
        pet_type_id = pet_type_id.fetchall()

        if len(product_type_id) == 0:
            print(product_type, "product type is invalid.")
        
        if len(pet_type_id) == 0:
            print("Pet type: %s is invalid.", pet_type)
            con.close()
            return
        
        # STILL WORKING ON THIS

        #if product_type == None:
        #    cur.execute("INSERT INTO products (name, product_type, pet_type, stock, price) VALUES(?, null, ?, ?, ?)", (name, pet_type, stock, price,))
        #else:
        cur.execute("INSERT INTO products (name, product_type, pet_type, stock, price) VALUES(?, ?, ?, ?, ?)", (name, product_type, pet_type, stock, price,))

        print(name,"product was added to the database.")
        print("\tProduct Type:", product_type)
        print("\tPet Type:", pet_type)
        print("\tStock:", stock)
        print("\tPrice:", price)




        
        con.commit()
        con.close()





    
    def deleteProduct(self, name):
        # Name: TEXT NOT NULL UNIQUE
        
        con = db.getDatabase()
        cur = con.cursor()

        
        con.commit()
        con.close()
        
    # ADOPTIONS
    def getAllAdoptions(self):
        con = db.getDatabase()
        cur = con.cursor()

        
        con.close()

    def getAdoption(self, id):

        con = db.getDatabase()
        cur = con.cursor()

        
        con.close()

    def addAdoption(self, type, price, availability, age, description):
        # Type: INTEGER
        # Availability: BOOLEAN
        # Age: INTEGER
        # Description: TEXT
        
        con = db.getDatabase()
        cur = con.cursor()

        cur.execute("INSERT INTO adoptions (type, availability, age, description) VALUES(?, ?, ?, ?)", (type, availability, age, description,))
        print(type,"adoption was added to the database.")
        print("\tAvailability:", availability)
        print("\tAge:", age)
        print("\tDescription:", description)
        

        
        con.commit()
        con.close()

    def deleteAdoption(self, id):
        con = db.getDatabase()
        cur = con.cursor()

        
        con.commit()
        con.close()

    # EMPLOYEES
    def getAllEmployees(self):
        con = db.getDatabase()
        cur = con.cursor()

        
        con.close()
    
    def getEmployee(self, name):
        con = db.getDatabase()
        cur = con.cursor()

        
        con.close()
    
    def addEmployee(self, name, department, shifts):
        # SHIFTS: FULL TIME / PART TIME (TEXT)
        # Name: TEXT
        # Department: TEXT NOT NULL UNIQUE
        # Shifts: TEXT
        
        con = db.getDatabase()
        cur = con.cursor()

        
        cur.execute("INSERT INTO employees (name, department, shifts) VALUES(?, ?, ?)", (name, department, shifts,))
        print(name,"is an employee that was added to the database.")
        print("\tDepartment:", department)
        print("\tShifts:", shifts)

        


        con.commit()
        con.close()
    
    def deleteEmployee(self, name):
        con = db.getDatabase()
        cur = con.cursor()

        
        con.commit()
        con.close()
    
    # EMPLOYEE SCHEDULES
    def getAllEmployeeSchedules(self):
        con = db.getDatabase()
        cur = con.cursor()

        
        con.close()
    
    def getEmployeeSchedule(self, name):
        con = db.getDatabase()
        cur = con.cursor()

        
        con.close()
    
    def addEmployeeSchedule(self, name, start, end):
        # Name: TEXT, UNIQUE
        # Start: INTEGER
        # End: INTEGER
        
        con = db.getDatabase()
        cur = con.cursor()

        
        cur.execute("INSERT INTO employees_schedules (name, start, end) VALUES(?, ?, ?)", (name, start, end,))
        print(name,"'s schedule was added to the database.")
        print("\tStart Time:", start)
        print("\tEnd Time:", end)

        con.commit()
        con.close()

    def deleteEmployeeSchedule(self, name):
        con = db.getDatabase()
        cur = con.cursor()

        
        con.commit()
        con.close()

    # CUSTOMERS
    def getAllCustomers(self):
        con = db.getDatabase()
        cur = con.cursor()

        
        con.close()

    def getCustomer(self, name):
        con = db.getDatabase()
        cur = con.cursor()

        
        con.close()

    def addCustomer(self, name, email, phone, pet_id):
        # Name: TEXT UNIQUE
        # Email: TEXT NOT NULL
        # Phone: TEXT NOT NULL
        # Pet_id: INTEGER
        con = db.getDatabase()
        cur = con.cursor()

        if pet_id == 0:
            cur.execute("INSERT INTO customers (name, email, phone_number, pet_id) VALUES(?, ?, ?, null)", (name, email, phone,))
        else:
            cur.execute("INSERT INTO customers (name, email, phone_number, pet_id) VALUES(?, ?, ?, ?)", (name, email, phone, pet_id))
        print(name," was added to the database as a customer.")
        print("\tEmail:", email)
        print("\tPhone:", phone)
        print("\tPet Id:", pet_id)
        
        con.commit()
        con.close()

    def deleteCustomer(self, name):
        con = db.getDatabase()
        cur = con.cursor()

        
        con.commit()
        con.close()
    
    # PETS
    def getAllPets(self):
        con = db.getDatabase()
        cur = con.cursor()

        
        con.close()

    def getPet(self, name):
        con = db.getDatabase()
        cur = con.cursor()

        
        con.close()

    def addPet(self, person_name, pet_name, age):
        # Person_name: TEXT NOT NULL
        # Pet_name: TEXT
        # Age: INTEGER
        con = db.getDatabase()
        cur = con.cursor()

        cur.execute("INSERT INTO pets (person_name, pet_name, age) VALUES(?, ?, ?)", (person_name, pet_name, age,))
        print(pet_name," was added to the database as the pet of", str(person_name)+".")
        print("\tAge:", age)

        con.commit()
        con.close()
    
    def deletePet(self, name):
        con = db.getDatabase()
        cur = con.cursor()



        con.commit()
        con.close()

    # SERVICES_SCHEDULE
    def getAllServices(self):
        con = db.getDatabase()
        cur = con.cursor()

        
        con.close()

    def getService(self, name):
        con = db.getDatabase()
        cur = con.cursor()


        con.close()

    def addService(self, type, pet_type, customer_name, start, end):
        # make an appointment

        # Type: TEXT NOT NULL UNIQUE
        # Pet_type: TEXT NOT NULL UNIQUE
        # Custumer_name: TEXT NOT NULL UNIQUE
        # Start: INTEGER
        # End: INTEGER
        con = db.getDatabase()
        cur = con.cursor()
        
        cur.execute("INSERT INTO services (type, pet_type, customer_name, start, end) VALUES(?, ?, ?, ?)", (type, pet_type, customer_name, start, end,))
        print(type," service was added to the database.")
        print("\tPet Type:", pet_type)
        print("\tCustomer Name:", customer_name)
        print("\tStart Time:", start)
        print("\tEnd Time:", end)


        con.commit()
        con.close()
    
    def deleteService(self, name):
        # delete an appointment
        con = db.getDatabase()
        cur = con.cursor()

        
        con.commit()
        con.close()
    
    # MEMBERSHIPS
    def getAllMemberships(self):
        con = db.getDatabase()
        cur = con.cursor()

        
    
        con.close()

    def getMembership(self, name):
        con = db.getDatabase()
        cur = con.cursor()

        
   
        con.close()

    def addMembership(self, name, active, years_subscribed):
        # Name: TEXT NOT NULL UNIQUE
        # Active: BOOL
        # Years_subscribed: INTEGER
        con = db.getDatabase()
        cur = con.cursor()

        customer_id = cur.execute("SELECT id FROM customers WHERE name = ?", (name,))
        customer_id = customer_id.fetchall()

        if len(customer_id) == 0:
            print("There is no customer with the name %s.", name)
            con.close()
            return
        
        # check if there is already an existing membership
        
        (customer_id,) = customer_id[0]
        cur.execute("INSERT INTO memberships (customer_id, active, years_subscribed) VALUES(?, ?, ?)", (customer_id, active, years_subscribed))
        print("name:",name,"with the membership was added to the database.")
        
        
        con.commit()
        con.close()
    
    def deleteMembership(self, name):
        con = db.getDatabase()
        cur = con.cursor()

        
        con.commit()
        con.close()

    # ROOMS
    def getAllRooms(self):
        con = db.getDatabase()
        cur = con.cursor()

        
        
        con.close()
        
    def getRoom(self, name):
        con = db.getDatabase()
        cur = con.cursor()


        con.close()
    
    def addRoom(self, name, service_type, employee_dept, description):
        # Name: TEXT NOT NULL UNIQUE
        # Service_type: TEXT NOT NULL UNIQUE
        # Employee_dept: TEXT NOT NULL UNIQUE
        # Description: TEXT
        con = db.getDatabase()
        cur = con.cursor()

        service_type_id = cur.execute("SELECT id FROM service_types WHERE type = ?", (service_type,))
        service_type_id = service_type_id.fetchall()
        employee_dept_id = cur.execute("SELECT id FROM employee_departments WHERE type = ?", (employee_dept,))
        employee_dept_id = employee_dept_id.fetchall()

        if len(service_type_id) == 0:
            print("There is no service type %s.", service_type)
        
        if len(employee_dept_id) == 0:
            print("There is no department type %s.", employee_dept)
            con.close()
            return
        
        (service_type_id,) = service_type_id[0]
        (employee_dept_id,) = employee_dept_id[0]

        cur.execute("INSERT INTO rooms (service_type_id, employee_dept_id, name, description) VALUES(?, ?, ?, ?)", (service_type_id, employee_dept_id, name, description,))
        print(name,"was added to the database.")

        con.commit()
        con.close()
    
    def deleteRoom(self, name):
        con = db.getDatabase()
        cur = con.cursor()

        
        con.commit()
        con.close()

    # INTERESTING QUERIES
    def mostExpensivePet(self):
        # looks for most expensive pet available for adoption

        con = db.getDatabase()
        cur = con.cursor()
        
        pet = cur.execute("""SELECT pet_types.type, pet_types.breed, adoptions.price, adoptions.description, adoptions.age
                    FROM adoptions
                    JOIN pet_types ON adoptions.pet_type_id = pet_types.id
                    ORDER BY adoptions.price DESC
                    LIMIT 1;
                    """)
        pet = cur.execute("""SELECT adoptions.price
        """)
        pet = pet.fetchall()
        if pet:
            print("Most Expensive Pet: Type:", pet[0], ", Breed:", pet[1], ", Age:", pet[4], ", Description:", pet[3])
        else:
            print("No pets available for adoption.")
        
        con.close()



    def giveCoupons():
        pass

    def displayEmployeeWeeklySchedule(self):

        con = db.getDatabase()
        cur = con.cursor()

        schedules = cur.execute("""
                    SELECT employees.name, employee_departments.type, employee_schedules.starting_time, employee_schedules.ending_time
                    FROM employee_schedules
                    JOIN employees ON employee_schedules.employee_id = employees.id
                    JOIN employee_departments ON employees.dept_id = employee_departments.id
                    ORDER BY employees.name, employee_schedules.starting_time
                """)
        employee_schedule = schedules.fetchall()
        if employee_schedule:
            print("Employee Weekly Schedules:")
            #not sure about this part im trying to unpack the tuple
            for schedule in schedules:
                employee, department, start, end = schedule
                print("Employee:",employee, ", Department:",department, ", Hours Working:", start, "AM to" ,end, "PM")
        else:
            print("No schedules found.")

        
        con.commit()
        con.close()


    def displayServicesWeeklySchedule():
        pass


    


    
