import pytest
from src.item import Item, InstantiateCSVError


def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError) as exc:
        Item.instantiate_from_csv('nonexistent_file.csv')
    assert str(exc.value) == "Отсутствует файл items.csv"

#
def test_instantiate_from_csv_corrupted_file():
    with pytest.raises(InstantiateCSVError) as exc:
        # Создаем файл и записываем в него данные
        with open('temp_corrupted_file.csv', 'w') as file:
            file.write("name,price,quantity\n")
            file.write("Laptop,1000,5\n")
            file.write("Mouse,200,")

        Item.instantiate_from_csv('temp_corrupted_file.csv')

    assert str(exc.value) == "Файл item.csv поврежден"