from faker import Faker
import random

from Src.complex_structures import Locations

N_StudentStatus = 2

Locations._read_from_file(Locations.directory_path + Locations.locations_filename)
fake = Faker()


def gen_Building():
    city_name, city = random.choice(list(Locations.cities.items()))
    street = random.choice(city.streets)
    return f"('{fake.color_name() + fake.city_suffix()}','{street.name}','{random.randint(1, 20)}','{city_name}','{street.postal_code}')"


def gen_Student():
    city_name, city = random.choice(list(Locations.cities.items()))
    street = random.choice(city.streets)
    return f"('{fake.first_name()}','{fake.last_name()}','{fake.iana_id()}','{fake.building_number()}','{fake.building_number()}','{street.name}','{city_name}','{street.postal_code}','{fake.ascii_email()}','{fake.phone_number()}','{random.randrange(N_StudentStatus)}')"


def gen_Employee():
    city_name, city = random.choice(list(Locations.cities.items()))
    street = random.choice(city.streets)
    return f"('{fake.first_name()}','{fake.last_name()}','{street.name}','{fake.building_number()}','{fake.building_number()}','{city_name}','{street.postal_code}','{fake.ascii_email()}','{fake.phone_number()}','{random.randrange(1000000) / 100.0}')"


def gen_Application(students, employees, applicationstatuses, utensils, applicationtypes):
    ID_Student = random.choice(students)
    ID_Employee = random.choice(employees)
    ID_ApplicationStatus = random.choice(applicationstatuses)
    ID_Utensils = random.choice(utensils)
    ID_ApplicationType = random.choice(applicationtypes)
    return f"('{ID_Student}','{ID_Employee}','{ID_ApplicationStatus}','{fake.date()}','{ID_Utensils}','{ID_ApplicationType}')"


def gen_Utensils(laundries, kitchens, rooms):
    ID_Laundry = random.choice(laundries)
    ID_Kitchen = random.choice(kitchens)
    ID_Room = random.choice(rooms)
    return f"('{fake.paragraph(nb_sentences=1)}','{random.randint(1, 8)}','{ID_Laundry}','{ID_Kitchen}','{ID_Room}')"


def gen_Floor(buildings):
    ID_Building = random.choice(buildings)
    return f"('{random.randint(0, 10)}','{ID_Building}')"


def gen_Room(modules):
    ID_Module = modules
    return f"('{random.randint(0, 999)}','{ID_Module}')"


def gen_Rent(rooms, students, applications):
    ID_Room = random.choice(rooms)
    ID_Student = random.choice(students)
    ID_Application = random.choice(applications)
    return f"('{ID_Room}','{ID_Student}','{ID_Application}','{fake.date()}')"


def gen_Charge(students):
    ID_Student = random.choice(students)
    return f"('{ID_Student}','{fake.date()}','{random.randrange(100000) / 100.0}')"


def gen_Payment(students):
    ID_Student = random.choice(students)
    return f"('{ID_Student}','{random.randrange(100000) / 100.0}','{fake.date()}')"


def gen_ParkingSpot(buildings):
    ID_Building = random.choice(buildings)
    return f"('{random.randint(1, 200)}','{ID_Building}')"


def gen_ResidentCard(parkingspots, students, cardstatuses):
    ID_ParkingSpot = random.choice(parkingspots)
    ID_Student = random.choice(students)
    ID_CardStatus = random.choice(cardstatuses)
    return f"('{ID_ParkingSpot}','{ID_Student}','{fake.date()}','{ID_CardStatus}')"


def gen_Building_Employee(employees, buildings):
    return None


def gen_Kitchen(floors):
    return None


def gen_Laundry(floors):
    return None


def gen_Module(floors):
    return None


def gen_Student_Status():
    return None


def gen_Application_Type():
    return None