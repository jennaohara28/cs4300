def calculate_discount(price, discount):
    return round(price - (price * (discount / 100)), 2)

def test_calculate_discount():
    assert calculate_discount(100, 30) == 70.0
    assert calculate_discount(75.99, 30.0) == 53.19