from faker import Faker
import random
import json
import csv

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

print(gen_Student())
print(gen_Employee())
print(gen_Building())
print(gen_Application(1,1,1,1,1))
