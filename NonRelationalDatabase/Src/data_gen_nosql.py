import string

from faker import Faker
from datetime import timedelta, datetime
import random

fake = Faker()


def generate_first_name():
    return fake.first_name()


def generate_last_name():
    return fake.last_name()


def generate_email():
    return fake.ascii_email()


def generate_phone():
    return fake.phone_number()


def generate_street():
    return fake.street_name()


def generate_city():
    return fake.city()


def generate_postal_code():
    return fake.zipcode()


def generate_item_name():
    return fake.product_name()


def generate_int(min, max):
    return random.randrange(min, max)


def generate_float(min, max):
    return round(random.uniform(min, max), 2)


def generate_date(start, stop):
    start = datetime.strptime(start, "%Y-%m-%d")
    stop = datetime.strptime(stop, "%Y-%m-%d")
    return datetime.combine(start + timedelta(days=random.randrange(0, (stop - start).days)), datetime.min.time())


def generate_random_string(x):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=x))