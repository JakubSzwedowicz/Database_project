from faker import Faker
import random
import json

fake = Faker()

N_StudentStatus = 2
N_ApplicationStatus = 3
N_Student = 200000
N_Employee = 4000
N_Kitchen = 2000
N_Laundry = 2000
N_Room = 50000

def gen_Building(id):
    return {
        'ID': id, 
        'Name': fake.color_name() + fake.city_suffix(), 
        'Street': fake.street_name(), 
        'BuildingNumber': random.randint(1,20), 
        'City': fake.city(), 
        'PostalCode': fake.postcode()
    }
  
def gen_Student(id):
    return {
        'ID': id,
        'Name': fake.first_name(),
        'LastName': fake.last_name(),
        'StudentNumber': fake.iana_id(),
        'BuildingNumber': fake.building_number(),
        'ApartmentNumber': fake.building_number(),
        'Street': fake.street_name(),
        'City': fake.city(),
        'PostalCode': fake.postcode(),
        'Email': fake.ascii_email(),
        'Phone': fake.phone_number(),
        'ID_StudentStatus': random.randrange(N_StudentStatus)
    }

def gen_Employee(id):
    return {
        'ID': id, 
        'Name': fake.first_name(), 
        'LastName': fake.last_name(), 
        'Street': fake.street_name(), 
        'ApartmentNumber': fake.building_number(), 
        'BuildingNumber': fake.building_number(), 
        'City': fake.city(), 
        'PostalCode': fake.postcode(), 
        'Email': fake.ascii_email(), 
        'Phone': fake.phone_number(), 
        'Salary': random.randrange(1000000)/100.0
    }

print(json.dumps(gen_Building(4), indent=3))
