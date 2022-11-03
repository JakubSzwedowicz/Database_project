# Author: Jakub Szwedowicz
# Date: 03.11.2022
# e-mail: kuba.szwedowicz@gmail.com

from database_tables import Tables
from faker import Faker
from pathlib import Path
import csv


class Locations:
    Faker.seed(1234)

    __DEFAULT_NUMBER_OF_CITIES = 100
    __DEFAULT_NUMBER_OF_STREETS_PER_CITY = 5
    __DEFAULT_NUMBER_OF_STREETS_PER_POSTAL_CODE = 3
    __faker = Faker()

    cities = {}
    directory_path = 'Resources/'
    locations_filename = 'locations.csv'

    class City:
        def __init__(self, name: str):
            self.name = name
            self.streets = []

    class Street:
        def __init__(self, name: str, postal_code: str):
            self.name = name
            self.postal_code = postal_code

    @classmethod
    def populate_locations(cls, filename: str = None) -> None:
        filepath = Locations.directory_path + (filename if filename is not None else Locations.locations_filename)

        file = Path(filepath)
        if file.is_file():
            Locations._read_from_file(filepath)
        else:
            Locations._generate_with_faker(filepath)

    @classmethod
    def _generate_with_faker(cls, filepath: str = None) -> None:
        with open(filepath, 'w') as f:
            for _ in range(Locations.__DEFAULT_NUMBER_OF_CITIES):
                city_name = Locations.__faker.city()
                city = Locations.City(city_name)
                postal_code = ''
                file_write_buffer = city_name
                for street_number in range(Locations.__DEFAULT_NUMBER_OF_STREETS_PER_CITY):
                    street_name = Locations.__faker.street_name()
                    if street_number % Locations.__DEFAULT_NUMBER_OF_STREETS_PER_POSTAL_CODE == 0:
                        postal_code = Locations.__faker.postcode()

                    street = Locations.Street(street_name, postal_code)
                    file_write_buffer += ';{0};{1}'.format(street.name, postal_code)
                    city.streets.append(street)

                Locations.cities[city_name] = city
                f.write(file_write_buffer + '\n')

    @classmethod
    def _read_from_file(cls, filepath: str = None) -> None:
        with open(filepath, newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            for row in reader:
                city, streets = Locations.City(row[0]), [Locations.Street(street_name, code) for (street_name, code) in
                                                         zip(row[1::2], row[2::2])]

                city.streets = streets
                Locations.cities[city.name] = city
