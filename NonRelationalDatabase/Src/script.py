from pymongo import MongoClient
from data_gen_nosql import *

client = MongoClient("mongodb+srv://mongo:54321@cluster0.9e7ffrw.mongodb.net/?retryWrites=true&w=majority")
db = client["Akademiki"]


def insert_users(count: int):
    print("insert users")

def get_random(list_of_values):
    return random.choice(list_of_values)


if __name__ == '__main__':
    # print(generate_first_names(10))
    print(generate_cities(5))
    print(generate_emails(5))
    print(generate_streets(5))
    print(generate_phones(5))
    print(generate_postal_codes(5))

