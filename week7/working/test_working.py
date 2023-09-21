from working import convert
import pytest


def test_valid_input_1():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_valid_input_2():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_valid_input_3():
    assert convert("12:30 PM to 1:45 AM") == "12:30 to 01:45"


def test_invalid_input_1():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")


def test_invalid_input_2():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")


def test_invalid_input_3():
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")
