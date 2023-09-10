import bank

def test_value():
    assert bank.value("hello") == int(0)
    assert bank.value("Hello") == int(0)
    assert bank.value("hey") == int(20)
    assert bank.value("yo") == int(100)
