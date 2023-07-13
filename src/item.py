import csv


class Item:

    pay_rate = 1
    instances = []

    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.instances.append(self)


    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def all(cls):
        return cls.instances

    # @classmethod
    # def get_instance_count(cls):
    #     return len(cls.instances)

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
        with open(file_path, 'r', encoding='Windows-1251') as file:
            csv_reader = csv.DictReader(file)
            next(csv_reader)  # Пропустить заголовки
            for row in csv_reader:
                name = row['name']
                price = row['price']
                quantity = row['quantity']
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(value):
        return int(float(value))

    @classmethod
    def delete_all_instances(cls):
        """Delete all instances"""
        cls.instances.clear()




