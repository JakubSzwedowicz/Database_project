from configparser import ConfigParser
import psycopg2

from Src import gen
from database_tables import Tables


def config(filename=r'C:\Users\Piotr\PycharmProjects\Database_project\Config\database.ini', section='postgresql'):
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
        cur.execute(sql, values)
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


# def insert_application():
#     values = Tables.generateApplication()
#     sql = f""" INSERT INTO application (id_student, id_employee, status, receivedate, id_applicationtype,
#                 id_utensils) VALUES {values} returning id"""
#     id = insert(sql, values)
#     return id
#
#
# def insert_payment():
#     values = Tables.generatePayment()
#     sql = f""" INSERT INTO payment (id_student, amount, paymentdate) VALUES {values} returning id"""
#     id = insert(sql, values)
#     return id
#
#
# def insert_charge():
#     values = Tables.generateCharge()
#     sql = f""" INSERT INTO charge (id_student, chargedate, amount) VALUES {values} returning id"""
#     id = insert(sql, values)
#     return id
#
#
# def insert_rent():
#     values = Tables.generateStudent()
#     sql = f""" INSERT INTO rent (id_room, id_student, id_application, expiredate) VALUES {values} returning id"""
#     id = insert(sql, values)
#     return id
#
#
# def insert_floor():
#     values = Tables.generateFloor()
#     sql = f""" INSERT INTO floor (number, id_building) VALUES {values} returning id"""
#     id = insert(sql, values)
#     return id
#
#
# def insert_kitchen():
#     values = Tables.generateKitchen()
#     sql = f""" INSERT INTO kitchen (id_floor) VALUES {values} returning id"""
#     id = insert(sql, values)
#     return id
#
#
# def insert_buildingemployee():
#     values = Tables.generateBuildingEmployee()
#     sql = f""" INSERT INTO building_employee (id_floor) VALUES {values} returning id"""
#     id = insert(sql, values)
#     return id
#
#
# def insert_laundry():
#     values = Tables.generateLaundry()
#     sql = f""" INSERT INTO laundry (id_floor) VALUES {values} returning id"""
#     id = insert(sql, values)
#     return id
#
#
# def insert_parkingspot():
#     values = Tables.generateParkingSpot()
#     sql = f""" INSERT INTO parkingspot (number, id_building) VALUES {values} returning id"""
#     id = insert(sql, values)
#     return id
#
#
# def insert_room():
#     values = Tables.generateRoom()
#     sql = f""" INSERT INTO room (number, id_module) VALUES {values} returning id"""
#     id = insert(sql, values)
#     return id
#
#
# def insert_module():
#     values = Tables.generateModule()
#     sql = f""" INSERT INTO module (id_floor) VALUES {values} returning id"""
#     id = insert(sql, values)
#     return id
#
#
# def insert_residentcard():
#     values = Tables.generateResidentCard()
#     sql = f""" INSERT INTO residentcard (id_parkingspot, id_student, expiredate, id_status) VALUES {values} returning id"""
#     id = insert(sql, values)
#     return id
#
#
# def insert_studentstatus():
#     values = Tables.generateStudentStatus()
#     sql = f""" INSERT INTO residentcard (status) VALUES {values} returning id"""
#     id = insert(sql, values)
#     return id
#
#
# def insert_applicationtype():
#     values = Tables.generateApplicationType()
#     sql = f""" INSERT INTO applicationtype (type) VALUES {values} returning id"""
#     id = insert(sql, values)
#     return id
#
#
# def insert_utensils():
#     values = Tables.generateUtensils()
#     sql = f""" INSERT INTO applicationtype (description, quantity, id_laundry, id_kitchen, id_room) VALUES {values} returning id"""
#     id = insert(sql, values)
#     return id
#
#
#
def populate_buildings(quantity):
    buildings = []
    for i in range(quantity):
        buildings.append(insert_building())

    return buildings
#
def populate_employee(quantity):
    result = []
    for i in range(quantity):
        result.append(insert_employee())

    return result

# def populate_rent(quantity):
#     result = []
#     for i in range(quantity):
#         result.append(insert_rent())
#
#     return result
#
# def populate_payment(quantity):
#     result = []
#     for i in range(quantity):
#         result.append(insert_payment())
#
#     return result
#
# def populate_charge(quantity):
#     result = []
#     for i in range(quantity):
#         result.append(insert_charge())
#
#     return result
#
# def populate_residentcard(quantity):
#     result = []
#     for i in range(quantity):
#         result.append(insert_residentcard())
#
#     return result
#
# def populate_kitchen(quantity):
#     result = []
#     for i in range(quantity):
#         result.append(insert_kitchen())
#
#     return result
#
# def populate_laundry(quantity):
#     result = []
#     for i in range(quantity):
#         result.append(insert_laundry())
#
#     return result
#
# def populate_module(quantity):
#     result = []
#     for i in range(quantity):
#         result.append(insert_module())
#
#     return result
#
# def populate_utensils(quantity):
#     result = []
#     for i in range(quantity):
#         result.append(insert_utensils())
#
#     return result
#
# def populate_buildingemployee(quantity):
#     result = []
#     for i in range(quantity):
#         result.append(insert_buildingemployee())
#
#     return result
#
# def populate_room(quantity):
#     result = []
#     for i in range(quantity):
#         result.append(insert_room())
#
#     return result
#
# def populate_floor(quantity):
#     result = []
#     for i in range(quantity):
#         result.append(insert_floor())
#
#     return result
#
# def populate_application(quantity):
#     result = []
#     for i in range(quantity):
#         result.append(insert_application())
#
#     return result
#
# def populate_parkingspot(quantity):
#     result = []
#     for i in range(quantity):
#         result.append(insert_parkingspot())
#
#     return result
#
# def populate_student(quantity):
#     result = []
#     for i in range(quantity):
#         result.append(insert_student())
#
#     return result


if __name__ == '__main__':
    buildings = populate_employee(3)

