import csv

from src.exceptions_class import InstantiateCSVError


class Item:

    pay_rate = 1
    instances = []

    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.instances.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name


    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def all(cls):
        return cls.instances

    @classmethod
    def get_instance_count(cls):
        return len(cls.instances)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) >= 10:
            self.__name = value[:10]
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls, file_path='src/items.csv'):
        try:
            with open(file_path, 'r', encoding='Windows-1251') as file:
                csv_reader = csv.DictReader(file)
                next(csv_reader)  # Пропустить заголовки
                for row in csv_reader:
                    name = row['name']
                    price = row['price']
                    quantity = row['quantity']
                    if not name or not price or not quantity:
                        raise InstantiateCSVError("Файл item.csv поврежден")
                    cls(name, price, quantity)
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл items.csv")

    @staticmethod
    def string_to_number(value):
        return int(float(value))

    @classmethod
    def delete_all_instances(cls):
        """Delete all instances"""
        cls.instances.clear()

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        else:
            raise TypeError("Can only add Item or Phone instances")
