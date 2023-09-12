from um import count


def test_count_match_um_in_words():
    assert count("mum") == 0


def test_count_require_spaces():
    assert count(" um ") == 1


def test_count_case():
    assert count("UM") == 1
