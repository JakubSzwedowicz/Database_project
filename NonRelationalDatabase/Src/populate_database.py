from pymongo import MongoClient
from bson import ObjectId
import random
import datetime
from data_gen_nosql import *

client = MongoClient("mongodb+srv://mongo:54321@cluster0.9e7ffrw.mongodb.net/?retryWrites=true&w=majority")
db = client["Akademiki"]

application_type = ['rent', 'parking_spot', 'utensils']
status = ['not sent', 'pending', 'accepted', 'declined']


def populate_users_student(count: int):
    students = []
    db_users = db['users']

    for i in range(count):
        user = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'street': fake.street_name(),
            'email': fake.email(),
            'phone_number': fake.phone_number(),
            'city': fake.city(),
            'postal_code': fake.zipcode(),
            'user_type': "student",
            'student_number': str(fake.random_number(digits=8)),
            'is_active': random.choice([True, False]),
            'payment': [],
            'charge': [],
        }
        # generate payment data
        for i in range(random.randint(1, 3)):
            payment = {
                'amount': round(random.uniform(0, 1000), 2),
                'payment_date': generate_date('2000-1-1', '2020-1-1')
            }
            user['payment'].append(payment)
        # generate charge data
        for i in range(random.randint(1, 3)):
            charge = {
                'amount': round(random.uniform(0, 1000), 2),
                'charge_date': generate_date('2000-1-1', '2020-1-1')
            }
            user['charge'].append(charge)

        students.append(user)

    db_users.insert_many(students)


def populate_users_employee(count: int):
    employees = []
    db_users = db['users']

    for i in range(count):
        user = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'street': fake.street_name(),
            'email': fake.email(),
            'phone_number': fake.phone_number(),
            'city': fake.city(),
            'postal_code': fake.zipcode(),
            'user_type': "employee",
            'salary': generate_float(1000.0, 10000.0)
        }
        employees.append(user)

    db_users.insert_many(employees)


def populate_buildings(count: int):
    buildings = []
    db_buildings = db['buildings']
    employees_from_db = list(db.users.find({"user_type": "employee"}))
    student_ids = [student["_id"] for student in db["users"].find({"user_type": "student"})]

    for i in range(count):
        building = {
            'name': fake.name(),
            'street': fake.street_name(),
            'building_number': fake.building_number(),
            'city': fake.city(),
            'postal_code': fake.zipcode(),
            'floors': [],
            'parking_spot': [],
            'employees': []
        }

        # Generate random employees
        for k in range(50, 100):
            building['employees'].append(random.choice(employees_from_db))

        # Generate floors and rooms
        for k in range(random.randint(7, 13)):
            floor = {
                'number': k + 1,
                'room': [],
                'utensils': []
            }
            for j in range(random.randint(15, 30)):
                room = {
                    'number': j + 1,
                    'occupants': random.sample(student_ids, random.randint(1, 3)),
                    'utensils': []
                }
                floor['room'].append(room)
            building['floors'].append(floor)

        # Generate parking spots
        for k in range(random.randint(30, 100)):
            parking_spot = {
                'number': k + 1,
                'owner_id': random.choice(student_ids)
            }
            building['parking_spot'].append(parking_spot)

        buildings.append(building)

    db_buildings.insert_many(buildings)


def populate_applications(count: int):
    db_applications = db['users_applications']
    applications = []

    student_ids = [student["_id"] for student in db["users"].find({"user_type": "student"})]
    employee_ids = [employee["_id"] for employee in db["users"].find({"user_type": "employee"})]

    for i in range(count):
        student_id = random.choice(student_ids)
        application = {
            "student_id": student_id,
            "applications": [
                {
                    "receive_date": generate_date('2000-1-1', '2020-1-1'),
                    "application_type": random.choice(["rent", "parking_spot", "utensils"]),
                    "application_history": [
                        {
                            "user_id": random.choice(employee_ids),
                            "date_of_change": generate_date('2000-1-1', '2020-1-1'),
                            "notes": "fake notes",
                            "status": random.choice(["not sent", "pending", "accepted", "declined"]),
                            "room_number": random.randint(1, 100),
                            "parking_spot_number": random.randint(1, 100),
                            "parking_spot_building_number": "fake building number",
                            "utensils": []
                        }
                    ]
                }
            ]
        }
        applications.append(application)

    db_applications.insert_many(applications)


if __name__ == '__main__':
    populate_users_student(20000)
    populate_users_employee(3000)
    populate_buildings(15)
    populate_applications(100000)
