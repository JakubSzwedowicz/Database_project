# Author: Jakub Szwedowicz
# Date: 02.11.2022
# e-mail: kuba.szwedowicz@gmail.com

import psycopg2
from configparser import ConfigParser
from database_tables import Tables
from complex_structures import Locations


def config(filename: str = 'Config/database.ini', section: str = 'postgresql') -> dict:
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


def connect():
    params = config()

    print('Connecting to the PostgreSQL database...')
    with psycopg2.connect(**params) as conn:
        with conn.cursor() as cur:
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            db_version = cur.fetchone()
            print(db_version)

            cur.close()
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def add_partv2(part_name, vendor_list):
    insert_part = 'INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id;'
    assign_vendor = 'INSERT INTO vendor_parts(vendor_id, part_id) VALUES(%s,%s)'

    params = config()
    with psycopg2.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute(insert_part, (part_name,))
            part_id = cur.fetchone()[0]

            for vendor_id in vendor_list:
                cur.execute(assign_vendor, (vendor_id, part_id))

            conn.commit()


def execute_add_part():
    add_partv2('SIM Tray', (1, 2))
    add_partv2('Speaker', (3, 4))
    add_partv2('Vibrator', (5, 6))
    add_partv2('Antenna', (6, 7))
    add_partv2('Home Button', (1, 5))
    add_partv2('LTE Modem', (1, 5))


def main():
    Tables.init_statuses()
    Locations.init_locations()

    # Tables.tables_example()
    Locations.locations_example()


if __name__ == '__main__':
    main()
