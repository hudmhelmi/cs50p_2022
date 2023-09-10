import twttr

def test_shorten():
    assert twttr.shorten("twitter") == "twttr"
    assert twttr.shorten("TWITTER") == "TWTTR"
    assert twttr.shorten("0") == "0"
    assert twttr.shorten(".") == "."    