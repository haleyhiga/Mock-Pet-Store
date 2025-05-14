# 🐾 The Haley & Hailey's Pet House

A mock pet store management system built with Python and SQLite, designed to handle various backend operations including inventory, services, scheduling, adoptions, and customer relations.

---

## Features

This project supports full CRUD operations and includes database interactions for:

- **Pet Types & Adoptions**
- **Product Types & Products**
- **Service Types & Scheduling**
- **Employees & Departments**
- **Employee & Service Schedules**
- **Customers & Memberships**
- **Coupons**
- **Rooms Management**

---

## Technologies Used

- **Python 3**
- **SQLite**
- Shell scripting (`populate.sh`)
- Command-line interface

---

## Project Structure

```
the-haley-haileys-pet-house/
├── PetHouse.db              # SQLite database file
├── db.py                    # Database connection and helper functions
├── main.py                  # Entry point for user interaction
├── pet_house.py             # All core business logic (functions for each entity)
├── populate.sh              # Optional script to seed initial data
├── testing.py               # Test functions (optional or for dev use)
```

---

## To Run:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/mock-pet-store.git
cd mock-pet-store/the-haley-haileys-pet-house
```

### 2. Run the Program

Make sure you have Python 3 installed.

```bash
python main.py
```

### 3. Populate Sample Data *(Optional)*

```bash
bash populate.sh
```

---

## Example Functions

Here are some example capabilities:

- Add a new pet:  
  `addPet(person_name="John", pet_name="Buddy", age=2)`

- Create a service appointment:  
  `addService(type="Grooming", pet_type="Dog", customer_name="John", start=10, end=12)`

- Retrieve all products:  
  `getAllProducts()`

---

## Authors

- Haley H.
- Hailey W.

---

