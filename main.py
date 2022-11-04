from configparser import ConfigParser
import psycopg2

from Src import gen


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


def insert(sql, values):
    conn = None
    id = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # execute SQL command
        cur.execute(sql, values)

        # receive id from database
        id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return id


def insert_building():
    values = gen.gen_Building()
    sql = f""" INSERT INTO building (name, street, buildingnumber, city, postalcode) VALUES {values} returning id"""
    id = insert(sql, values)
    return id


def insert_student():
    values = gen.gen_Student()
    sql = f""" INSERT INTO student (name, lastname, studentnumber, buildingnumber, apartmentnumber, street, 
                city, postalcode, email, phone) VALUES {values} returning id"""
    id = insert(sql, values)
    return id


def insert_employee():
    values = gen.gen_Employee()
    sql = f""" INSERT INTO employee (name, lastname, street, apartmentnumber, buildingnumber, city, postalcode, email,
            phone, salary) VALUES {values} returning id"""
    id = insert(sql, values)
    return id


def insert_application(students, employees, applications_statuses, utensils, application_types):
    values = gen.gen_Application(students, employees, applications_statuses, utensils, application_types)
    sql = f""" INSERT INTO application (id_student, id_employee, status, receivedate, id_applicationtype,
                id_utensils) VALUES {values} returning id"""
    id = insert(sql, values)
    return id


def insert_payment(students):
    values = gen.gen_Payment(students)
    sql = f""" INSERT INTO payment (id_student, amount, paymentdate) VALUES {values} returning id"""
    id = insert(sql, values)
    return id


def insert_charge(students):
    values = gen.gen_Charge(students)
    sql = f""" INSERT INTO charge (id_student, chargedate, amount) VALUES {values} returning id"""
    id = insert(sql, values)
    return id


def insert_rent(rooms, students, applications):
    values = gen.gen_Rent(rooms, students, applications)
    sql = f""" INSERT INTO rent (id_room, id_student, id_application, expiredate) VALUES {values} returning id"""
    id = insert(sql, values)
    return id


def insert_floor(buildings):
    values = gen.gen_Floor(buildings)
    sql = f""" INSERT INTO floor (number, id_building) VALUES {values} returning id"""
    id = insert(sql, values)
    return id


def insert_kitchen(floors):
    values = gen.gen_Kitchen(floors)
    sql = f""" INSERT INTO kitchen (id_floor) VALUES {values} returning id"""
    id = insert(sql, values)
    return id


def insert_building_employee(employees, buildings):
    values = gen.gen_Building_Employee(employees, buildings)
    sql = f""" INSERT INTO building_employee (id_floor) VALUES {values} returning id"""
    id = insert(sql, values)
    return id


def insert_laundry(floors):
    values = gen.gen_Laundry(floors)
    sql = f""" INSERT INTO laundry (id_floor) VALUES {values} returning id"""
    id = insert(sql, values)
    return id


def insert_parking_spot(buildings):
    values = gen.gen_ParkingSpot(buildings)
    sql = f""" INSERT INTO parkingspot (number, id_building) VALUES {values} returning id"""
    id = insert(sql, values)
    return id


def insert_room(modules):
    values = gen.gen_Room(modules)
    sql = f""" INSERT INTO room (number, id_module) VALUES {values} returning id"""
    id = insert(sql, values)
    return id


def insert_module(floors):
    values = gen.gen_Module(floors)
    sql = f""" INSERT INTO module (id_floor) VALUES {values} returning id"""
    id = insert(sql, values)
    return id


def insert_resident_card(parking_spots, students, card_statuses):
    values = gen.gen_ResidentCard(parking_spots, students, card_statuses)
    sql = f""" INSERT INTO residentcard (id_parkingspot, id_student, expiredate, id_status) 
            VALUES {values} returning id"""
    id = insert(sql, values)
    return id


def insert_student_status():
    values = gen.gen_Student_Status()
    sql = f""" INSERT INTO residentcard (status) VALUES {values} returning id"""
    id = insert(sql, values)
    return id


def insert_application_type():
    values = gen.gen_Application_Type()
    sql = f""" INSERT INTO applicationtype (type) VALUES {values} returning id"""
    id = insert(sql, values)
    return id


def insert_utensils(laundries, kitchens, rooms):
    values = gen.gen_Utensils(laundries, kitchens, rooms)
    sql = f""" INSERT INTO applicationtype (description, quantity, id_laundry, id_kitchen, id_room) 
            VALUES {values} returning id"""
    id = insert(sql, values)
    return id


def populate_buildings(quantity):
    buildings = []
    for i in range(quantity):
        buildings.append(insert_building())

    return buildings


def populate_employees(quantity):
    result = []
    for i in range(quantity):
        result.append(insert_employee())

    return result


def populate_rents(quantity, rooms, students, applications):
    result = []
    for i in range(quantity):
        result.append(insert_rent(rooms, students, applications))

    return result


def populate_payments(quantity, students):
    result = []
    for i in range(quantity):
        result.append(insert_payment(students))

    return result


def populate_charges(quantity, students):
    result = []
    for i in range(quantity):
        result.append(insert_charge(students))

    return result


def populate_resident_cards(quantity, parking_spots, students, card_statuses):
    result = []
    for i in range(quantity):
        result.append(insert_resident_card(parking_spots, students, card_statuses))

    return result


def populate_kitchens(quantity, floors):
    result = []
    for i in range(quantity):
        result.append(insert_kitchen(floors))

    return result


def populate_laundries(quantity, floors):
    result = []
    for i in range(quantity):
        result.append(insert_laundry(floors))

    return result


def populate_modules(quantity, floors):
    result = []
    for i in range(quantity):
        result.append(insert_module(floors))

    return result


def populate_utensils(quantity, laundries, kitchens, rooms):
    result = []
    for i in range(quantity):
        result.append(insert_utensils(laundries, kitchens, rooms))

    return result


def populate_building_employee(quantity, buildings, employees):
    result = []
    for i in range(quantity):
        result.append(insert_building_employee(buildings, employees))

    return result


def populate_rooms(quantity, modules):
    result = []
    for i in range(quantity):
        result.append(insert_room(modules))

    return result


def populate_floors(quantity, buildings):
    result = []
    for i in range(quantity):
        result.append(insert_floor(buildings))

    return result


def populate_applications(quantity, students, employees, applications_statuses, utensils, application_types):
    result = []
    for i in range(quantity):
        result.append(insert_application(students, employees, applications_statuses, utensils, application_types))

    return result


def populate_parking_spots(quantity, buildings):
    result = []
    for i in range(quantity):
        result.append(insert_parking_spot(buildings))

    return result


def populate_students(quantity):
    result = []
    for i in range(quantity):
        result.append(insert_student())

    return result


if __name__ == '__main__':
    buildings = populate_buildings(10)
    floors = populate_floors(20, buildings)
    kitchens = populate_kitchens(20, floors)
    laundries = populate_laundries(20, floors)
    modules = populate_modules(20, floors)
    rooms = populate_rooms(20, modules)
    utensils = populate_utensils(50, laundries, kitchens, rooms)
    parking_spots = populate_parking_spots(20, buildings)

    students = populate_students(10)
    payments = populate_payments(20, students)
    charges = populate_charges(20, students)

    # wpisac to z palca?
    card_statuses = [1, 2]
    application_statuses = [1, 2, 3, 4]
    application_types = [1, 2, 3, 4]
    resident_cards = populate_resident_cards(50, parking_spots, charges, card_statuses)

    employees = populate_employees(20)
    applications = populate_applications(10, students, employees, application_statuses, utensils, application_types)
    buildings_employees = populate_building_employee(30, buildings, employees)
