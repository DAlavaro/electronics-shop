from src.item import Item



def test_calculate_total_price():
    item = Item("Смартфон", 10000, 20)
    assert item.calculate_total_price() == 200000

def test_apply_discount():
    item = Item("Смартфон", 10000, 20)
    item.apply_discount()
    assert item.price == 10000  # без скидки

    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000  # со скидкой


def test_all():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    items = Item.all()
    assert item1 in items
    assert item2 in items

def test_name():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмарт'

def test_instantiate_from_csv():

    Item.instantiate_from_csv()
    assert len(Item.all()) == 9

    item1 = Item.all()[5]
    assert item1.name == 'Ноутбук'

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5