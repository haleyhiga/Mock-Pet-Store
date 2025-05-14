# Designed by Haley Higa and Hailey Whipple.

import click
import pet_house
import os

# COLOR SCHEME
Dark_Pink = (217, 139, 153)
Light_Pink = (242, 201, 209)
Grey_Pink = (217, 180, 187)
White_Pink = (242, 223, 226)
Dark_Brown = (89, 77, 77)

# Dark_Pink, Light_Pink, Grey_Pink, White_Pink, Dark_Brown

PET_STORE_NAME = "PetHouse"
DB_FILE = PET_STORE_NAME + ".db"
PET_HOUSE = pet_house.PetHouse(False)

if os.path.exists(DB_FILE):
    PET_HOUSE = pet_house.PetHouse(True)

#
# DATABASE MANAGEMENT
#

@click.group()
def database_management():
    pass

@click.group()
def pet_types():
    pass

@click.group()
def service_types():
    pass

@click.group()
def product_types():
    pass

@click.group()
def employee_departments():
    pass

@click.group()
def coupons():
    pass

@click.group()
def products():
    pass

@click.group()
def adoptions():
    pass

@click.group()
def employees():
    pass

@click.group()
def employee_schedules():
    pass

@click.group()
def customers():
    pass

@click.group()
def pets():
    pass

@click.group()
def services_schedule():
    pass

@click.group()
def memberships():
    pass

@click.group()
def rooms():
    pass

@click.group()
def interesting_queries():
    pass

#
#   DATABASE MANAGEMENT
#

@click.command()
def createDB():
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
    PET_HOUSE.createDatabase()

@click.command()
def deleteDB():
    PET_HOUSE.deleteDatabase()

@click.command()
def getTables():
    tables = PET_HOUSE.getTables()
    print(tables)



#
#   PET TYPES
#



@click.command()
def get_all_pet_types():
    PET_HOUSE.getAllPetTypes()
@click.command()
@click.argument('type')
def get_pet_type(type):
    PET_HOUSE.getPetType(type)
@click.command()
@click.argument('type')
@click.argument('breed')
def add_pet_type(type, breed):
    PET_HOUSE.addPetType(type, breed)
@click.command()
@click.argument('type')
def delete_pet_type(type):
    PET_HOUSE.deletePetType(type)



#
#   SERVICE_TYPES
#



@click.command()
def get_all_service_types():
    PET_HOUSE.getAllServiceTypes()
@click.command()
@click.argument('type')
def get_service_type(type):
    PET_HOUSE.getServiceType(type)
@click.command()
@click.argument('type')
@click.argument('plan')
@click.argument('description')
@click.argument('price', type=int)
def add_service_type(type, plan, description, price):
    PET_HOUSE.addServiceType(type, plan, description, price)
@click.command()
@click.argument('type')
def delete_service_type(type):
    PET_HOUSE.deleteServiceType(type)



#
#   PRODUCT TYPES
#



@click.command()
def get_all_product_types():
    PET_HOUSE.getAllProductTypes()
@click.command()
@click.argument('type')
def get_product_type(type):
    PET_HOUSE.getProductType(type)
@click.command()
@click.argument('type')
@click.argument('description')
def add_product_type(type, description):
    PET_HOUSE.addProductType(type, description)
@click.command()
@click.argument('type')
def delete_product_type(type):
    PET_HOUSE.deleteProductType(type)
    


#
#   EMPLOYEE DEPARTMENTS
#



@click.command()
def get_all_employee_departments():
    PET_HOUSE.getAllEmployeeDepartments()
@click.command()
@click.argument('type')
def get_employee_department(type):
    PET_HOUSE.getEmployeeDepartment(type)
@click.command()
@click.argument('type')
@click.argument('description')
def add_employee_department(type, description):
    PET_HOUSE.addEmployeeDepartment(type, description)
@click.command()
@click.argument('type')
def delete_employee_department(type):
    PET_HOUSE.deleteEmployeeDepartment(type)



#
#   COUPONS
#



@click.command()
def get_all_coupons():
    PET_HOUSE.getAllCoupons()
@click.command()
@click.argument('name')
def get_coupon(name):
    PET_HOUSE.getCoupon(name)
@click.command()
@click.argument('name')
@click.argument('type')
@click.argument('start')
@click.argument('end')
@click.argument('constraints')
def add_coupon(name, type, start, end, constraints):
    PET_HOUSE.addCoupon(name, type, start, end, constraints)
@click.command()
@click.argument('name')
def delete_coupon(name):
    PET_HOUSE.deleteCoupon(name)



#
#   PRODUCTS
#



@click.command()
def get_all_products():
    PET_HOUSE.getAllProducts()
@click.command()
@click.argument('name')
def get_product(name):
    PET_HOUSE.getProduct(name)
@click.command()
@click.argument('name')
@click.argument('type')
@click.argument('pet_type')
@click.argument('stock', type=int)
@click.argument('price', type=int)
def add_product(name, product_type, pet_type, stock, price):
    PET_HOUSE.addProduct(name, product_type, pet_type, stock, price)
@click.command()
@click.argument('name')
def delete_product(name):
    PET_HOUSE.deleteProduct(name)



#
#   ADOPTIONS
#



@click.command()
def get_all_adoptions():
    PET_HOUSE.getAllAdoptions()
@click.command()
@click.argument('id', type=int)
def get_adoption(id):
    PET_HOUSE.getAdoption(id)
@click.command()
@click.argument('type')
@click.argument('price', type=int)
@click.argument('availability', type=bool)
@click.argument('age', type=int)
@click.argument('description')
def add_adoption(type, price, availability, age, description):
    PET_HOUSE.addAdoption(type, price, availability, age, description)
@click.command()
@click.argument('id')
def delete_adoption(id):
    PET_HOUSE.deleteAdoption(id)



#
#   EMPLOYEES
#



@click.command()
def get_all_employees():
    PET_HOUSE.getAllEmployees()
@click.command()
@click.argument('name')
def get_employee(name):
    PET_HOUSE.getEmployee(name)
@click.command()
@click.argument('name')
@click.argument('department')
@click.argument('shifts')
def add_employee(name, department, shifts):
    PET_HOUSE.addEmployee(name, department, shifts)
@click.command()
@click.argument('name')
def delete_employee(name):
    PET_HOUSE.deleteEmployee(name)



#
#   EMPLOYEE SCHEDULES
#



@click.command()
def get_all_employee_schedules():
    PET_HOUSE.getAllEmployeeSchedules()
@click.command()
@click.argument('name')
def get_employee_schedule(name):
    PET_HOUSE.getEmployeeSchedule(name)
@click.command()
@click.argument('name')
@click.argument('start')
@click.argument('end')
def add_employee_schedule(name, start, end):
    PET_HOUSE.addEmployeeSchedule(name, start, end)
@click.command()
@click.argument('name')
def delete_employee_schedule(name):
    PET_HOUSE.deleteEmployeeSchedule(name)


#
#   CUSTOMERS
#



@click.command()
def get_all_customers():
    PET_HOUSE.getAllCustomers()
@click.command()
@click.argument('name')
def get_customer(name):
    PET_HOUSE.getCustomer(name)
@click.command()
@click.argument('name')
@click.argument('email')
@click.argument('phone_number')
@click.argument('pet_id', type=int)
def add_customer(name, email, phone_number, pet_id):
    PET_HOUSE.addCustomer(name, email, phone_number, pet_id)
@click.command()
@click.argument('name')
def delete_customer(name):
    PET_HOUSE.delete_customer(name)



#
#   PETS
#



@click.command()
def get_all_pets():
    PET_HOUSE.getAllPets()
@click.command()
@click.argument('name')
def get_pet(name):
    PET_HOUSE.getPet(name)
@click.command()
@click.argument('person_name')
@click.argument('pet_name')
@click.argument('age', type=int)
def add_pet(person_name, pet_name, age):
    PET_HOUSE.addPet(person_name, pet_name, age)
@click.command()
@click.argument('name')
def delete_pet(name):
    PET_HOUSE.deletePet(name)



#
#   SERVICES
#



@click.command()
def get_all_services():
    PET_HOUSE.getAllServices()
@click.command()
@click.argument('name')
def get_service(name):
    PET_HOUSE.getService(name)
@click.command()
@click.argument('type')
@click.argument('pet_type')
@click.argument('customer_name')
@click.argument('start')
@click.argument('end')
def add_service(type, pet_type, customer_name, start, end):
    PET_HOUSE.addService(type, pet_type, customer_name, start, end)
@click.command()
@click.argument('name')
def delete_service(name):
    PET_HOUSE.deleteService(name)
    


#
#   MEMBERSHIP COMMANDS
#



@click.command()
def get_all_memberships():
    PET_HOUSE.getAllMemberships()
@click.command()
@click.argument('name')
def get_membership(name):
    PET_HOUSE.getMembership(name)
@click.command()
@click.argument('name')
@click.argument('active', type=bool)
@click.argument('years_subscribed', type=int)
def add_membership(name, active, years_subscribed):
    PET_HOUSE.addMembership(name, active, years_subscribed)
@click.command()
@click.argument('name')
def delete_membership(name):
    PET_HOUSE.deleteMembership()



#
#   ROOM COMMANDS
#



@click.command()
def get_all_rooms():
    PET_HOUSE.getAllRooms()
@click.command()
@click.argument('name')
def get_rooms(name):
    PET_HOUSE.getRoom(name)
@click.command()
@click.argument('name')
@click.argument('service_type')
@click.argument('employee_dept')
@click.argument('description')
def add_rooms(name, service_type, employee_dept, description):
    PET_HOUSE.addRoom(name, service_type, employee_dept, description)
@click.command()
@click.argument('name')
def delete_rooms(name):
    PET_HOUSE.deleteRoom(name)



#
#   INTERESTING QUERIES
#

@click.command()
#@click.argument('')
def most_expensive_pet():
    PET_HOUSE.mostExpensivePet()

@click.command()
#@click.argument('')
def give_coupons():
    PET_HOUSE.giveCoupons()

@click.command()
def display_employee_weekly_schedule():
    PET_HOUSE.displayEmployeeWeeklySchedule()

@click.command()
def display_services_weekly_schedule():
    PET_HOUSE.displayServicesWeeklySchedule()


def introduction(database_exists):
    if not database_exists:
        return '''\n\t[Currently, there is no existing database.]
\tTo create a database, use the following command:
\t\tcreateDB
\tTo delete the database, use the following command:
\t\tdeleteDB
\tHave fun shopping or please visit some of our services!
'''
    elif database_exists:
        return '''\n\n\t[Currently, there is an existing database.]
\tTo create a database, use the following command:\n
\t\tcreateDB\n

\tTo delete the database, use the following command:\n
\t\tdeleteDB\n\n
\tHave fun shopping or please visit some of our services!
'''

        
def custom_format_usage(ctx, formatter):
    # Dark_Pink, Light_Pink, Grey_Pink, White_Pink, Dark_Brown
    exists = os.path.exists(DB_FILE)
    
    name = ctx.info_name
    heading_string = "    🐶🐱🐟    Welcome to the [Haley/Hailey]'s Pet House!    🐶🐱🐟    \n"
    database_string = ""
    if exists:
        database_string = "     [Currently, there is an existing database.]" # 1 new line
    elif not exists:
        database_string = "     [Currently, there is no existing database.]" # 1 new line
            
    create = "     To create a database, use the following command:" # 1 new line
    create_cmd = "          createDB" # 1 new line

    delete = "     To delete the database, use the following command:" # 1 new line
    delete_cmd = "          deleteDB" # 1 new lines
    have_fun = "     Have fun shopping or please visit some of our services!"

    length_of_heading = len(heading_string)+5
    database_string = database_string + (" "* (length_of_heading - len(database_string))) 
    create = create + (" "* (length_of_heading - len(create)) )
    create_cmd = create_cmd + (" "* (length_of_heading - len(create_cmd)) )
    delete = delete + (" "* (length_of_heading - len(delete)) )
    delete_cmd = delete_cmd + (" "* (length_of_heading - len(delete_cmd)))
    empty_line = " " * length_of_heading
    have_fun = have_fun + (" "* (length_of_heading - len(have_fun)))

    database_string += "\n"
    create += "\n"
    create_cmd += "\n"
    delete += "\n"
    delete_cmd += "\n"
    empty_line += "\n"
    have_fun += "\n"

    first = click.style("\n", fg=Dark_Pink, bg=White_Pink)
    empty = click.style(empty_line, fg=Dark_Pink, bg=White_Pink)
    heading = click.style(heading_string, fg=Dark_Pink, bg=White_Pink, bold=True)
    intro = click.style(empty_line+database_string+create+create_cmd+delete+delete_cmd+empty_line+have_fun, fg=Dark_Pink, bg=White_Pink)
    
    formatter.write(first)
    formatter.write(empty)
    formatter.write(heading)
    formatter.write(intro)
    formatter.write(first)
    formatter.write(first)
    formatter.write("\n\n")

    #formatter.write_text("-"*length_of_heading)
    #formatter.write_text("~"*length_of_heading)
    #formatter.write_text("-"*length_of_heading)
    formatter.write_text(f"Usage: {name} [OPTIONS] COMMAND [ARGS]...\n")
    formatter.color = True

if __name__ == '__main__':
    '''
    if not os.path.exists(DB_FILE):
        db.createDatabase()
    '''

    database_management.add_command(createDB, "create")
    database_management.add_command(deleteDB, "delete")
    database_management.add_command(getTables, "tables")

    pet_types.add_command(get_all_pet_types, "get-all-pet-types")
    pet_types.add_command(get_pet_type, "get-pet-type")
    pet_types.add_command(add_pet_type, "add-pet-type")
    pet_types.add_command(delete_pet_type, "delete-pet-type")
    
    service_types.add_command(get_all_service_types, "get-all-service-types")
    service_types.add_command(get_service_type, "get-service-type")
    service_types.add_command(add_service_type, "add-service-type")
    service_types.add_command(delete_service_type, "delete-service-type")
    
    product_types.add_command(get_all_product_types, "get-all-product-types")
    product_types.add_command(get_product_type, "get-product-type")
    product_types.add_command(add_product_type, "add-product-type")
    product_types.add_command(delete_product, "delete-product")
    
    employee_departments.add_command(get_all_employee_departments, "get-all-employee")
    employee_departments.add_command(get_employee_department, "get-employee-department")
    employee_departments.add_command(add_employee_department, "add-employee-department")
    employee_departments.add_command(delete_employee_department, "delete-employee-department")
    
    coupons.add_command(get_all_coupons, "get-all-coupons")
    coupons.add_command(get_coupon, "get-coupon")
    coupons.add_command(add_coupon, "add-coupon")
    coupons.add_command(delete_coupon, "delete-coupon")
    
    products.add_command(get_all_products, "get-all-products")
    products.add_command(get_product, "get-product")
    products.add_command(add_product, "add-product")
    products.add_command(delete_product, "delete-product")
    
    adoptions.add_command(get_all_adoptions, "get-all-adoptions")
    adoptions.add_command(get_adoption, "get-adoption")
    adoptions.add_command(add_adoption, "add-adoption")
    adoptions.add_command(delete_adoption, "delete-adoption")
    
    employees.add_command(get_all_employees, "get-all-employees")
    employees.add_command(get_employee, "get-employee")
    employees.add_command(add_employee, "add-employee")
    employees.add_command(delete_employee, "delete-employee")
    
    employee_schedules.add_command(get_all_employee_schedules, "get-all-employee-schedules")
    employee_schedules.add_command(get_employee_schedule, "get-employee-schedule")
    employee_schedules.add_command(add_employee_schedule, "add-employee-schedule")
    employee_schedules.add_command(delete_employee_schedule, "delete-employee-schedule")
    
    customers.add_command(get_all_customers, "get-all-customers")
    customers.add_command(get_customer, "get-customer")
    customers.add_command(add_customer, "add-customer")
    customers.add_command(delete_customer, "delete-customer")
    
    pets.add_command(get_all_pets, "get-all-pets")
    pets.add_command(get_pet, "get-pet")
    pets.add_command(add_pet, "add-pet")
    pets.add_command(delete_pet, "delete-pet")
    
    services_schedule.add_command(get_all_services, "get-all-services")
    services_schedule.add_command(get_service, "get-service")
    services_schedule.add_command(add_service, "add-service")
    services_schedule.add_command(delete_service, "delete-service")
    
    memberships.add_command(get_all_memberships, "get-all-memberships")
    memberships.add_command(get_membership, "get-membership")
    memberships.add_command(add_membership, "add-membership")
    memberships.add_command(delete_membership, "delete-membership")
    
    rooms.add_command(get_all_rooms, "get-all-rooms")
    rooms.add_command(get_rooms, "get-room")
    rooms.add_command(add_rooms, "add-room")
    rooms.add_command(delete_rooms, "delete-room")

    interesting_queries.add_command(most_expensive_pet, "most-expensive-pet")
    interesting_queries.add_command(give_coupons, "give-coupons")
    interesting_queries.add_command(display_employee_weekly_schedule, "display-employee-schedule")
    interesting_queries.add_command(display_services_weekly_schedule, "display-services-schedule")

    cli = click.CommandCollection(sources=[database_management, pet_types, service_types, product_types, employee_departments, coupons, products, adoptions, employees, employee_schedules, customers, pets, services_schedule, memberships, rooms])
    cli.format_usage = custom_format_usage
    cli()

#python3 ./main.py