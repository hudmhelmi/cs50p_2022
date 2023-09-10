import pytest

from fuel import convert, gauge


def test_convert_returns_correct_ints():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75


def test_convert_raises_value_error_for_invalid_fractions():
    with pytest.raises(ValueError):
        convert("abc")
    with pytest.raises(ValueError):
        convert("2/1")


def test_convert_raises_zero_division_error_for_fractions_with_denominator_of_0():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge_labels_1_as_e():
    assert gauge(1) == "E"


def test_gauge_prints_percentage():
    assert gauge(50) == "50%"


def test_gauge_labels_99_as_f():
    assert gauge(99) == "F"
