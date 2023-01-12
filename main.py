from configparser import ConfigParser
import psycopg2
from psycopg2.extras import execute_values

import gen


def config(filename=r"./Config/database.ini", section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def insert_many(insert_query, data):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        psycopg2.extras.execute_values(cur, insert_query, data)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def populate_buildings(quantity):
    data = list()
    for i in range(quantity):
        data.append(gen.gen_Building())

    formatted_data = list(map(eval, data))
    insert_query = "INSERT INTO building (name, street, buildingnumber, city, postalcode) VALUES %s"
    insert_many(insert_query, formatted_data)
    return list(range(1,quantity+1))


def populate_employees(quantity):
    data = list()
    for i in range(quantity):
        data.append(gen.gen_Employee())

    formatted_data = list(map(eval, data))
    insert_query = "INSERT INTO employee (name, lastname, street, apartmentnumber, buildingnumber," \
                   " city, postalcode, email, phone, salary) VALUES %s"
    insert_many(insert_query, formatted_data)
    return list(range(1,quantity+1))


def populate_rents(quantity, rooms, students, applications):
    data = list()
    for i in range(quantity):
        data.append(gen.gen_Rent(rooms, students, applications))

    formatted_data = list(map(eval, data))
    insert_query = "INSERT INTO rent (id_room, id_student, id_application, expiredate) VALUES %s"
    insert_many(insert_query, formatted_data)
    return list(range(1,quantity+1))


def populate_payments(quantity, students):
    data = list()
    for i in range(quantity):
        data.append(gen.gen_Payment(students))

    formatted_data = list(map(eval, data))
    insert_query = "INSERT INTO payment (id_student, amount, paymentdate) VALUES %s"
    insert_many(insert_query, formatted_data)
    return list(range(1,quantity+1))


def populate_charges(quantity, students):
    data = list()
    for i in range(quantity):
        data.append(gen.gen_Charge(students))

    formatted_data = list(map(eval, data))
    insert_query = "INSERT INTO charge (id_student, chargedate, amount) VALUES %s"
    insert_many(insert_query, formatted_data)
    return list(range(1, quantity+1))


def populate_resident_cards(quantity, parking_spots, students, card_statuses):
    data = list()
    for i in range(quantity):
        data.append(gen.gen_ResidentCard(parking_spots, students, card_statuses))

    formatted_data = list(map(eval, data))
    insert_query = "INSERT INTO residentcard (id_parkingspot, id_student, expiredate, id_cardstatus) VALUES %s"
    insert_many(insert_query, formatted_data)
    return list(range(1,quantity+1))


def populate_kitchens(quantity, floors):
    data = list()
    for i in range(quantity):
        data.append(gen.gen_Kitchen(floors))
    formatted_data = list(map(eval, data))
    insert_query = "INSERT INTO kitchen (id_floor) VALUES %s"
    insert_many(insert_query, formatted_data)
    return list(range(1, quantity+1))


def populate_laundries(quantity, floors):
    data = list()
    for i in range(quantity):
        data.append(gen.gen_Laundry(floors))

    formatted_data = list(map(eval, data))
    insert_query = "INSERT INTO laundry (id_floor) VALUES %s"
    insert_many(insert_query, formatted_data)
    return list(range(1,quantity+1))


def populate_modules(quantity, floors):
    data = list()
    for i in range(quantity):
        data.append(gen.gen_Module(floors))

    formatted_data = list(map(eval, data))
    insert_query = "INSERT INTO module (id_floor) VALUES %s"
    insert_many(insert_query, formatted_data)
    return list(range(1,quantity+1))


def populate_utensils(quantity, laundries, kitchens, rooms):
    data = list()
    for i in range(quantity):
        data.append(gen.gen_Utensils(laundries, kitchens, rooms))

    formatted_data = list(map(eval, data))
    insert_query = "INSERT INTO utensils (description, quantity, id_laundry, id_kitchen, id_room) VALUES %s"
    insert_many(insert_query, formatted_data)
    return list(range(1,quantity+1))


def populate_building_employee(quantity, buildings, employees):
    data = list()
    for i in range(quantity):
        data.append(gen.gen_Building_Employee(buildings, employees))

    formatted_data = list(map(eval, data))
    insert_query = "INSERT INTO building_employee (id_building, id_employee) VALUES %s"
    insert_many(insert_query, formatted_data)
    return list(range(1,quantity+1))


def populate_rooms(quantity, modules):
    data = list()
    for i in range(quantity):
        data.append(gen.gen_Room(modules))

    formatted_data = list(map(eval, data))
    insert_query = "INSERT INTO room (number, id_module) VALUES %s"
    insert_many(insert_query, formatted_data)
    return list(range(1,quantity+1))


def populate_floors(quantity, buildings):
    data = list()
    for i in range(quantity):
        data.append(gen.gen_Floor(buildings))

    formatted_data = list(map(eval, data))
    insert_query = "INSERT INTO floor (number, id_building) VALUES %s"
    insert_many(insert_query, formatted_data)
    return list(range(1,quantity+1))


def populate_applications(quantity, students, employees, applications_statuses, utensils, application_types):
    data = list()
    for i in range(quantity):
        data.append(gen.gen_Application(students, employees, applications_statuses, utensils, application_types))
    formatted_data = list(map(eval, data))
    insert_query = "INSERT INTO application (id_student, id_employee, id_applicationstatus, receivedate, id_utensils, id_applicationtype) VALUES %s"
    insert_many(insert_query, formatted_data)
    return list(range(1,quantity+1))


def populate_parking_spots(quantity, buildings):
    data = list()
    for i in range(quantity):
        data.append(gen.gen_ParkingSpot(buildings))

    formatted_data = list(map(eval, data))
    insert_query = "INSERT INTO parkingspot (number, id_building) VALUES %s"
    insert_many(insert_query, formatted_data)
    return list(range(1,quantity+1))


def populate_students(quantity):
    data = list()
    for i in range(quantity):
        data.append(gen.gen_Student())

    formatted_data = list(map(eval, data))
    insert_query = "INSERT INTO student (name, lastname, studentnumber, buildingnumber, apartmentnumber, street, city, postalcode, email, phone, id_studentstatus) VALUES %s"
    insert_many(insert_query, formatted_data)
    return list(range(1,quantity+1))


if __name__ == '__main__':
    buildings = populate_buildings(70)
    floors = populate_floors(5000, buildings)
    kitchens = populate_kitchens(5000, floors)
    laundries = populate_laundries(5000, floors)
    modules = populate_modules(25000, floors)
    rooms = populate_rooms(50000, modules)
    utensils = populate_utensils(100000, laundries, kitchens, rooms)
    parking_spots = populate_parking_spots(5000, buildings)

    students = populate_students(50000)
    payments = populate_payments(100000, students)
    charges = populate_charges(100000, students)


    card_statuses = [1, 2]
    application_statuses = [1, 2, 3, 4]
    application_types = [1, 2, 3, 4]
    resident_cards = populate_resident_cards(4000, parking_spots, students, card_statuses)

    employees = populate_employees(3000)
    applications = populate_applications(100000, students, employees, application_statuses, utensils, application_types)
    buildings_employees = populate_building_employee(1000, buildings, employees)
    rents = populate_rents(50000, rooms, students, applications)