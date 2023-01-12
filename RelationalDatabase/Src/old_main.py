import psycopg2
from configparser import ConfigParser


def config(filename: str = 'database.ini', section: str = 'postgresql') -> dict:
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
    conn = None
    try:
        params = config()

        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def create_tables():
    commands = (
        """
        CREATE TABLE vendors (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE parts (
                part_id SERIAL PRIMARY KEY,
                part_name VARCHAR(255) NOT NULL
                )
        """,
        """
        CREATE TABLE part_drawings (
                part_id INTEGER PRIMARY KEY,
                file_extension VARCHAR(5) NOT NULL,
                drawing_data BYTEA NOT NULL,
                FOREIGN KEY (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE vendor_parts (
                vendor_id INTEGER NOT NULL,
                part_id INTEGER NOT NULL,
                PRIMARY KEY (vendor_id , part_id),
                FOREIGN KEY (vendor_id)
                    REFERENCES vendors (vendor_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (part_id)
                    REFERENCES parts (part_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        for command in commands:
            cur.execute(command)

        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_vendor(vendor_name):
    sql = """INSERT INTO vendors(vendor_name)
            VALUES(%s) RETURNING vendor_id;"""

    conn = None
    vendor_id = None

    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        cur.execute(sql, (vendor_name,))

        vendor_id = cur.fetchone()[0]

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return vendor_id


def insert_vendor_list(vendor_list):
    sql = 'INSERT INTO vendors(vendor_name) VALUES(%s)'
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.executemany(sql, vendor_list)

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def execute_insert_vendor_list():
    insert_vendor('3M Co.')

    insert_vendor_list([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])


def add_part(part_name, vendor_list):
    insert_part = 'INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id;'
    assign_vendor = 'INSERT INTO vendor_parts(vendor_id, part_id) VALUES(%s,%s)'

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(insert_part, (part_name,))
        part_id = cur.fetchone()[0]

        for vendor_id in vendor_list:
            cur.execute(assign_vendor, (vendor_id, part_id))

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def add_partv2(part_name, vendor_list):
    insert_part = 'INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id;'
    assign_vendor = 'INSERT INTO vendor_parts(vendor_id, part_id) VALUES(%s,%s)'

    params = config()
    with psycopg2.connect(**params) as conn:
        with conn.cursor as cur:
            cur.execute(insert_part, (part_name,))
            part_id = cur.fetchone()[0]

            for vendor_id in vendor_list:
                cur.execute(assign_vendor, (vendor_id, part_id))

            conn.commit()
        if conn is not None:
            conn.close()


def execute_add_part():
    add_part('SIM Tray', (1,2))
    add_part('Speaker', (3,4))
    add_part('Vibrator', (5,6))
    add_part('Antenna', (6,7))
    add_part('Home Button', (1,5))
    add_part('LTE Modem', (1,5))

def main():
    execute_add_part()


if __name__ == '__main__':
    main()
