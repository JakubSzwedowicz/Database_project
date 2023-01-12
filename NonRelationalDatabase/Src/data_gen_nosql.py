from faker import Faker
from datetime import timedelta, datetime
import random

fake = Faker()


def generate_first_names(count: int):
    return [fake.first_name() for x in range(count)]


def generate_last_names(count: int):
    return [fake.last_name() for x in range(count)]


def generate_emails(count: int):
    return [fake.ascii_email() for x in range(count)]


def generate_phones(count: int):
    return [fake.phone_number() for x in range(count)]


def generate_streets(count: int):
    return [fake.street_name() for x in range(count)]


def generate_cities(count: int):
    return [fake.city() for x in range(count)]


def generate_postal_codes(count: int):
    return [fake.zipcode() for x in range(count)]


def generate_ints(count, min, max):
    return [random.randrange(min, max) for x in range(count)]


def generate_floats(count, min, max):
    return [round(random.uniform(min, max), 2) for x in range(count)]


def generate_dates(count, start, stop):
    start = datetime.strptime(start, "%Y-%m-%d")
    stop = datetime.strptime(stop, "%Y-%m-%d")
    return [(start+timedelta(days=random.randrange(0, (stop-start).days))) for x in range(count)]