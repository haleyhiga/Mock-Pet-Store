'''
Creates random data and tests it for the database.
'''

emails = []
names = []
amount = 10

import random
import faker
import petname

fake = faker.Faker()

first_names = [fake.first_name() for _ in range(50)]
last_names = [fake.last_name() for _ in range(50)]

full_names = [f"{first_name} {last_name}" for first_name, last_name in zip(first_names, last_names)]


pet_names = [
    "Apollo", "Juno", "Marley", "Tinkerbell", "Zeus", 
    "Olive", "Bandit", "Luna", "Rusty", "Peaches", 
    "Dexter", "Hazel", "Beau", "Poppy", "Casper", 
    "Muffin", "Harley", "Pearl", "Finn", "Cleopatra", 
    "Thor", "Willow", "Biscuit", "Ivy", "Baxter", 
    "Daisy", "Winston", "Pumpkin", "Bruno", "Olive", 
    "Hercules", "Hazel", "Sprout", "Winston", "Lulu", 
    "Gizmo", "Honey", "Duke", "Maple", "Hercules", 
    "Penelope", "Finnegan", "Lilo", "Rusty", "Juniper", 
    "Scooter", "Noodle", "Whiskers", "Pippin", "Clementine"
]

names = full_names
for name in full_names:
    n = name.split(" ")
    first, last = n[0], n[1]
    final = first+"."+last+"@gmail.com"
    emails.append(final.lower())

# COMMANDS
    
def commands(AMOUNT_OF_COMMANDS):
    file = open('populate.sh', 'w')

    intro = "python3 ./main.py "

    # Adding to the database
    add_adoption = intro+"add-adoption"
    add_coupon = intro+"add-coupon"
    add_customer = intro+"add-customer"
    add_employee = intro+"add-employee"
    add_employee_dept = intro+"add-employee-department"
    add_employee_schedule = intro+"add-employee-schedule"
    add_membership = intro+"add-membership"
    add_pet = intro+"add-pet"
    add_pet_type = intro+"add-pet-type"
    add_product = intro+"add-product"
    add_product_type = intro+"add-product_type"
    add_room = intro+"add-room"
    add_service = intro+"add-service"
    add_service_type = intro+"add-service-type"

    #
    # COMMANDS THAT CHANGE DATABASE
    #

    EMPLOYEE_DEPARTMENTS = ["Information Technology", "Customer Service", "Animal Caretakers"]

    EMPLOYEE_DEPARTMENTS_DESCRIPTION = ["Responsible for ensuring the smooth operation of the stores technology infrastructure, including point-of-sale systems, inventory management software, and customer relationship management tools.", "The customer service department for a pet store aims to provide helpful and informative assistance to customers, addressing their queries and concerns related to pet care, products, and services.", "Responsible for ensuring the well-being and health of the animals in the store. They feed, water, groom, bathe, exercise, and provide care to promote the overall health and happiness of the pets, which may include dogs, cats, fish, birds, and other small animals. The caretakers also keep records of feedings, treatments, and animals received or discharged, and are responsible for cleaning and disinfecting enclosures, as well as performing routine maintenance tasks to ensure a safe and healthy environment for both the animals and customers."]

    EMPLOYEES_EMAILS = ["rizzross@vim.com","emacslover@emacs.com","hawaiianshirtlover@thonny.com","housebuilder@vscode.com", "applevisionuser@vscode.com", "sweetheart@thonny.com", "socslover@vim.com"]

    EMPLOYEES_NAMES = ["Russ Ross", "Curtis Larsen", "Bart Stander", "Lora Klein", "Matt Kearl", "Carol Stander", "Ren Quinn"]

    n = 0
    while n < len(EMPLOYEE_DEPARTMENTS):
        #add-employee-department
        type = str(EMPLOYEE_DEPARTMENTS[n])
        description = str(EMPLOYEE_DEPARTMENTS_DESCRIPTION[n])
        s = add_employee_dept + " " + type + " " + description + "\n"
        file.write(s)
        n += 1

    # EMPLOYEES_EMAILS, EMPLOYEES_NAMES
    n = 0
    while n < len(EMPLOYEES_NAMES):
        #add_employee
        name = str(EMPLOYEES_NAMES[n])

        if n < 3:
            department = str(EMPLOYEE_DEPARTMENTS[0])
        elif n > 2 and n < 4:
            department = str(EMPLOYEE_DEPARTMENTS[1])
        else:
            department = str(EMPLOYEE_DEPARTMENTS[2])

        if name != "Lora Klein":
            shifts = str("Full")
        else:
            shifts = str("Part")

        s = add_employee + " " + name + " " + department + " " + shifts + "\n"
        file.write(s)

        #add_employee_schedule
        if name != "Lora Klein":
            start = str(9)
            end = str(5)
        else:
            start = str(9)
            end = str(1)
        s = add_employee_schedule + " " + name + " " + start + " " + end + "\n"
        file.write(s)

        n += 1

    PETS = {
        "fish": ["parrotfish", "angelfish", "pufferfish", "beta", "goldfish"], 
        "dog": ["golden doodle", "golden retriever", "chihuahua", "pomeranian"],
        "bird": ["cockatiel", "parrot", "cockatoo", "parakeet"],
        "chicken": ["silkie", "brahma", "bantam", "sebright"],
        "turtle": ["pond slider", "caramel albino red eared slider", "eastern box", "painted", "false map", "snapping", "african aquatic sideneck"], 
        "hamster": ["syrian", "campbell's dwarf", "roborovski dwarf", "winter white dwarf", "chinese", "gansu"], 
        "cat": ["bobtail", "balinese", "persian", "tabby", "siberian"], 
        "other": ["hedgehog", "bunny", "lizard"]
    }
    
    for type in PETS:
        #add_pet_type
        type = str(type)
        for breed in PETS[type]:
            s = add_pet_type + " " + type + " " + breed + "\n"
            file.write(s)

    n = 0
    while n < len(names):
        #add_pet
        person_name = str(names[n])
        pet_name = str(petname.Generate())
        age = str()
        s = add_pet + " " + person_name + " " + pet_name + " " + age + "\n"
        file.write(s)

#
# https://pypi.org/project/petname/2.2/
#

        #add_customer
        name = str(names[n])
        email = str(emails[n])
        fake.seed(0)
        phone = str(fake.phone_number())
        pet_id = str()
        s = add_customer + " " + name + " " + email + " " + phone + " " + pet_id + "\n"
        file.write(s)

        n += 1
    
    i = 0
    
    while i < AMOUNT_OF_COMMANDS:

        # add-adoption
        type = str()
        price = str()
        availability = str()
        age = str()
        description = str()
        s = add_adoption + " " + type + " " + availability + " " + age +  " " + description + "\n"
        file.write(s)
        
        #add_coupon
        name = str()
        type = str()
        start = str()
        end = str()
        constraints = str()
        s = add_coupon + " " + name + " " + type + " " + start + " " + end + " " + constraints + "\n"
        file.write(s)

        #add_membership
        name = str()
        active = str()
        years_subscribed = str()
        s = add_membership + " " + name + " " + active + " " + years_subscribed + "\n"
        file.write(s)

        #add_product
        name = str()
        product_type = str()
        pet_type = str()
        stock = str()
        price = str()
        s = add_product + " " + name + " " + product_type + " " + pet_type + " " + stock + " " + price + "\n"
        file.write(s)

        #add_product_type
        type = str()
        description = str()
        s = add_product + " " + type + " " + description + "\n"
        file.write(s)

        #add_room
        name = str()
        service_type = str()
        employee_dept = str()
        description = str()
        s = add_room + " " + name + " " + service_type + " " + employee_dept + " " + description + "\n"
        file.write(s)

        #add_service
        type = str()
        pet_type = str()
        customer_name = str()
        start = str()
        end = str()
        s = add_service_type + " " + type + " " + pet_type + " " + customer_name + " " + start + " " + end + "\n"
        file.write(s)

        #add_service_type
        type = str()
        plan = str()
        description = str()
        price = str()
        s = add_service_type + " " + type + " " + plan + " " + description + " " + price + "\n"
        file.write(s)

        i += 1


    #file.write("rm -f Turtle.db")
    file.close()

# chmod u+x add-users.sh
# bash add-users.sh

# chmod u+x add-accounts.sh
# bash add-accounts.sh
    
# chmod u+x add-posts.sh
# bash add-posts.sh
    
# chmod u+x input.sh
# bash input.sh

# python3 ./main.py

def main():
    commands(amount)
main()