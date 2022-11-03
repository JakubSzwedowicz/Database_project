from faker import Faker
import random
import json
import csv

from complex_structures import Locations
Locations._read_from_file(Locations.directory_path+Locations.locations_filename)

fake = Faker()

N_StudentStatus = 2
N_ApplicationStatus = 3
N_Student = 200000
N_Employee = 4000
N_Kitchen = 2000
N_Laundry = 2000
N_Room = 50000

def gen_Building(id):
    city_name, city = random.choice(list(Locations.cities.items()))
    street = random.choice(city.streets)
    return {
        'ID': id, 
        'Name': fake.color_name() + fake.city_suffix(), 
        'Street': street.name, 
        'BuildingNumber': random.randint(1,20), 
        'City': city_name, 
        'PostalCode': street.postal_code
    }
  
def gen_Student(id):
    city_name, city = random.choice(list(Locations.cities.items()))
    street = random.choice(city.streets)
    return {
        'ID': id,
        'Name': fake.first_name(),
        'LastName': fake.last_name(),
        'StudentNumber': fake.iana_id(),
        'BuildingNumber': fake.building_number(),
        'ApartmentNumber': fake.building_number(),
        'Street': street.name,
        'City': city_name,
        'PostalCode': street.postal_code,
        'Email': fake.ascii_email(),
        'Phone': fake.phone_number(),
        'ID_StudentStatus': random.randrange(N_StudentStatus)
    }

def gen_Employee(id):
    city_name, city = random.choice(list(Locations.cities.items()))
    street = random.choice(city.streets)
    return {
        'ID': id, 
        'Name': fake.first_name(), 
        'LastName': fake.last_name(), 
        'Street': street.name, 
        'ApartmentNumber': fake.building_number(), 
        'BuildingNumber': fake.building_number(), 
        'City': city_name, 
        'PostalCode': street.postal_code, 
        'Email': fake.ascii_email(), 
        'Phone': fake.phone_number(), 
        'Salary': random.randrange(1000000)/100.0
    }

print(gen_Student(6))
print(gen_Employee(6))
print(gen_Building(6))
