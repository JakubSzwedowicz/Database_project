# Author: Jakub Szwedowicz
# Date: 02.11.2022
# e-mail: kuba.szwedowicz@gmail.com
import datetime
import random
from enum import Enum
from decimal import Decimal


class Tables:
    _is_initialized = False

    @classmethod
    def init_statuses(cls) -> None:
        Tables.StudentStatus.build_instances()
        Tables.ApplicationType.build_instances()
        Tables.ApplicationStatus.build_instances()
        Tables.CardStatus.build_instances()
        cls._is_initialized = True

    @classmethod
    def tables_statuses_example(cls) -> None:
        if not cls._is_initialized:
            cls.init_statuses()
        print([x.status for x in Tables.StudentStatus.get_all_instances()])
        print([x.status for x in Tables.ApplicationType.get_all_instances()])
        print([x.status for x in Tables.ApplicationStatus.get_all_instances()])
        print([x.status for x in Tables.CardStatus.get_all_instances()])

    @classmethod
    def is_initialized(cls) -> bool:
        return cls._is_initialized

    class BaseTable:
        def __init__(self):
            self.uid = None

        def complete_instance(self, uid: int):
            self.uid = uid

    class Base2Table:
        def __init__(self):
            self.uid1 = None
            self.uid2 = None

        def complete_instance(self, uid1: int, uid2: int):
            self.uid1 = uid1
            self.uid2 = uid2

    class Application(BaseTable):
        def __init__(self, id_student: int, id_employee: int, id_application_status: int,
                     receive_date: datetime.date, id_utensils: int, id_application_type: int):
            super().__init__()
            self.id_student = id_student
            self.id_employee = id_employee
            self.id_application_status = id_application_status
            self.receive_date = receive_date
            self.id_utensils = id_utensils
            self.id_application_type = id_application_type

    class Student(BaseTable):
        def __int__(self, name: str, last_name: str, student_numer: str, building_number: str,
                    apartment_number: str, street: str, city: str, postal_code: str, email: str, phone: str):
            super().__init__()
            self.name = name
            self.last_name = last_name
            self.student_numer = student_numer
            self.building_number = building_number
            self.apartment_number = apartment_number
            self.street = street
            self.city = city
            self.postal_code = postal_code
            self.email = email
            self.phone = phone

    class Employee(BaseTable):
        def __int__(self, name: str, last_name: str, street: str,
                    apartment_number: str, building_number: str, city: str, postal_code: str, email: str,
                    phone: str, salary: Decimal):
            super().__init__()
            self.name = name
            self.last_name = last_name
            self.street = street
            self.apartment_number = apartment_number
            self.building_number = building_number
            self.city = city
            self.postal_code = postal_code
            self.email = email
            self.phone = phone
            self.salary = salary

    class Utensils(BaseTable):
        def __init__(self, description: str, quantity: int, id_laundry: int, id_kitchen: int, id_room: int):
            super().__init__()
            self.description = description
            self.quantity = quantity
            self.id_laundry = id_laundry
            self.id_kitchen = id_kitchen
            self.id_room = id_room

    class Laundry(BaseTable):
        def __init__(self, id_pietra: int):
            super().__init__()
            self.id_pietra = id_pietra

    class Floor(BaseTable):
        def __init__(self, number: int, id_building: int):
            super().__init__()
            self.number = number
            self.id_building = id_building

    class Building(BaseTable):
        def __init__(self, name: str, street: str, building_number: int, city: str, postal_code: str):
            super().__init__()
            self.name = name
            self.street = street
            self.building_number = building_number
            self.city = city
            self.postal_code = postal_code

    class Kitchen(BaseTable):
        def __init__(self, id_floor: int):
            super().__init__()
            self.id_floor = id_floor

    class Room(BaseTable):
        def __init__(self, number: int, id_module: int):
            super().__init__()
            self.number = number
            self.id_module = id_module

    class Module(BaseTable):
        def __init__(self, id_floor: int):
            super().__init__()
            self.id_floor = id_floor

    class Rent(BaseTable):
        def __init__(self, id_room: int, id_student: int, id_application: int, expire_date: datetime.date):
            super().__init__()
            self.id_room = id_room
            self.id_student = id_student
            self.id_application = id_application
            self.expire_date = expire_date

    class Charge(BaseTable):
        def __init__(self, id_student: int, charge_date: datetime.date, amount: Decimal):
            if amount <= 0:
                raise Exception('Illegal amount {0}'.format(amount))

            super().__init__()
            self.id_student = id_student
            self.charge_date = charge_date
            self.amount = amount

    class Payment(BaseTable):
        def __init__(self, id_student: int, amount: Decimal, payment_date: datetime.date):
            if amount <= 0:
                raise Exception('Illegal amount {0}'.format(amount))
            super().__init__()
            self.id_student = id_student
            self.amount = amount
            self.payment_date = payment_date

    class ParkingSpot(BaseTable):
        def __init__(self, number: int, id_building: int):
            if number <= 0:
                raise Exception('Illegal number {0}'.format(number))
            super().__init__()
            self.number = number
            self.id_building = id_building

    class ResidentCard(BaseTable):
        def __init__(self, id_parking_spot: int, id_student: int, expire_date: datetime.date, id_card_status: int):
            super().__init__()
            self.id_parking_spot = id_parking_spot
            self.id_student = id_student
            self.expire_date = expire_date
            self.id_card_status = id_card_status

    class Building_Employee(Base2Table):
        def __init__(self):
            super().__init__()

    class Status(BaseTable):
        _instances: list = []
        _enum_fields = Enum

        def __init__(self, status: Enum):
            super().__init__()
            self.status = status

        @classmethod
        def build_instances(cls):
            for enum in cls._enum_fields:
                status = cls(enum.value)
                cls._add_instance(status)

        @classmethod
        def get_all_instances(cls) -> list:
            return cls._instances

        @classmethod
        def generate_status(cls, index: int = None) -> str:
            max_index = len(cls._instances) - 1
            if index is not None:
                if index > max_index:
                    raise Exception('Index {0} out of bound [0, {1}]'.format(index, max_index))
            else:
                index = random.randint(0, max_index)
            return f"('{cls._instances[index].status}')"

        @classmethod
        def _add_instance(cls, status):
            cls._instances.append(status)

    class StudentStatus(Status):
        class StudentStatusEnumeration(Enum):
            ACTIVE = 'active student'
            FINISHED = 'finished university'
            REVOKED = 'student status revoked'

        _instances: list = []
        _enum_fields = StudentStatusEnumeration

        def __init__(self, status: StudentStatusEnumeration):
            super().__init__(status)

    class ApplicationType(Status):
        class ApplicationTypeEnumeration(Enum):
            PARKING_SPACE = 'application for parking space'
            DORM = 'application for a room in dormitory'

        _instances: list = []
        _enum_fields = ApplicationTypeEnumeration

        def __init__(self, status: ApplicationTypeEnumeration):
            super().__init__(status)

    class ApplicationStatus(Status):
        class ApplicationStatusEnumeration(Enum):
            PENDING = 'pending'
            ACCEPTED = 'accepted'
            DECLNED = 'declined'

        _instances: list = []
        _enum_fields = ApplicationStatusEnumeration

        def __init__(self, status: ApplicationStatusEnumeration):
            super().__init__(status)

    class CardStatus(Status):
        class CardStatusEnumeration(Enum):
            VALID = 'valid'
            INVALID = 'invalid'

        _instances: list = []
        _enum_fields = CardStatusEnumeration

        def __init__(self, status: CardStatusEnumeration):
            super().__init__(status)
