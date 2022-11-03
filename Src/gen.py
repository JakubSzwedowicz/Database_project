from faker import Faker
import random

from complex_structures import Locations

N_StudentStatus = 2

Locations._read_from_file(Locations.directory_path+Locations.locations_filename)
fake = Faker()

def gen_Building():
    city_name, city = random.choice(list(Locations.cities.items()))
    street = random.choice(city.streets)
    return f"('{fake.color_name() + fake.city_suffix()}','{street.name}','{random.randint(1,20)}','{city_name}','{street.postal_code}')"
  
def gen_Student():
    city_name, city = random.choice(list(Locations.cities.items()))
    street = random.choice(city.streets)
    return f"('{fake.first_name()}','{fake.last_name()}','{fake.iana_id()}','{fake.building_number()}','{fake.building_number()}','{street.name}','{city_name}','{street.postal_code}','{fake.ascii_email()}','{fake.phone_number()}','{random.randrange(N_StudentStatus)}')"

def gen_Employee():
    city_name, city = random.choice(list(Locations.cities.items()))
    street = random.choice(city.streets)
    return f"('{fake.first_name()}','{fake.last_name()}','{street.name}','{fake.building_number()}','{fake.building_number()}','{city_name}','{street.postal_code}','{fake.ascii_email()}','{fake.phone_number()}','{random.randrange(1000000)/100.0}')"

def gen_Application(ID_Student, ID_Employee, ID_ApplicationStatus, ID_Utensils, ID_ApplicationType):
    return f"('{ID_Student}','{ID_Employee}','{ID_ApplicationStatus}','{fake.date()}','{ID_Utensils}','{ID_ApplicationType}')"

def gen_Utensils(ID_Laundry, ID_Kitchen, ID_Room):
    return f"('{fake.paragraph(nb_sentences=1)}','{random.randint(1,8)}','{ID_Laundry}','{ID_Kitchen}','{ID_Room}')"

def gen_Floor(ID_Building):
    return f"('{random.randint(0,10)}','{ID_Building}')"

def gen_Room(ID_Module):
    return f"('{random.randint(0,999)}','{ID_Module}')"

def gen_Rent(ID_Room, ID_Student, ID_Application):
    return f"('{ID_Room}','{ID_Student}','{ID_Application}','{fake.date()}')"

def gen_Charge(ID_Student):
    return f"('{ID_Student}','{fake.date()}','{random.randrange(100000)/100.0}')"

def gen_Payment(ID_Student):
    return f"('{ID_Student}','{random.randrange(100000)/100.0}','{fake.date()}')"

def gen_ParkingSpot(ID_Building):
    return f"('{random.randint(1,200)}','{ID_Building}')"

def gen_ResidentCard(ID_ParkingSpot, ID_Student, ID_CardStatus):
    return f"('{ID_ParkingSpot}','{ID_Student}','{fake.date()}','{ID_CardStatus}')" 
