import pytest

from src.phone import Phone


def test_repr_and_str():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2

def test_number_of_sim_error():
    with pytest.raises(ValueError) as exc:
        phone = Phone("Смартфон", 10000, 10, 2)
        phone.number_of_sim = 0
    assert exc
