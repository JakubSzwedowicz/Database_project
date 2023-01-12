from pymongo import MongoClient


database_name = 'Akademiki'


def get_database():
    # https://www.mongodb.com/languages/python
    password = 54321

    connection_string = f'mongodb+srv://mongo:{password}@cluster0.9e7ffrw.mongodb.net/?retryWrites=true&w=majority'

    client = MongoClient(connection_string)

    return client[database_name]


if __name__ == '__main__':
    db = get_database()
    print(db.name)