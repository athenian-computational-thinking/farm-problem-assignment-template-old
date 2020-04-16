from my_code import legs


def test_inc():
    assert 10 == legs(2,2,2)
    assert 34 == legs(5,2,4)
    assert 22 == legs(1,3,2)
