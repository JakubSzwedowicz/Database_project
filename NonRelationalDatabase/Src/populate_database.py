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
    user_ids = [user["_id"] for user in db.users.find({}, {"_id": 1})]

    for i in range(count):
        building = {
            'name': fake.name(),
            'street': fake.street_name(),
            'building_number': fake.building_number(),
            'city': fake.city(),
            'postal_code': fake.zipcode(),
            'floors': [],
            'parking_spot': []
        }

        # Generate floors and rooms
        for i in range(random.randint(1, 5)):
            floor = {
                'number': i + 1,
                'room': [],
                'utensils': []
            }
            for j in range(random.randint(1, 10)):
                room = {
                    'number': j + 1,
                    'occupants': random.sample(user_ids, random.randint(1, 3)),
                    'utensils': []
                }
                floor['room'].append(room)
            building['floors'].append(floor)

        # Generate parking spots
        for i in range(random.randint(1, 10)):
            parking_spot = {
                'number': i + 1,
                'owner_id': random.choice(user_ids)
            }
            building['parking_spot'].append(parking_spot)

        buildings.append(building)

    db_buildings.insert_many(buildings)


if __name__ == '__main__':
    # populate_users_student(10)
    # populate_users_employee(10)
    populate_buildings(10)
