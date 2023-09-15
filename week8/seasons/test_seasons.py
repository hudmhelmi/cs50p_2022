from seasons import convert_to_text
from datetime import date, timedelta
import pytest


def test_convert_to_text_valid():
    assert (
        convert_to_text(timedelta(days=365))
        == "minus five hundred and twenty-five thousand, six hundred"
    )


def test_convert_to_text_invalid():
    with pytest.raises(AttributeError):
        convert_to_text("February 6th, 1998")
