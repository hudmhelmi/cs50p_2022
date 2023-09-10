from plates import is_valid

def test_valid():
    assert is_valid("AAA111") is True

def test_alphabetical():
    assert is_valid("11111") is False

def test_too_short():
    assert is_valid("A") is False

def test_too_long():
    assert is_valid("AAA11111") is False

def test_starts_with_number():
    assert is_valid("1AAA111") is False

def test_number_in_the_middle():
    assert is_valid("AAA2AA") is False

def test_zero():
    assert is_valid("AA0000") is False

def test_non_alphanumeric():
    assert is_valid("AAA!11") is False
