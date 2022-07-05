import pytest

@pytest.mark.great
def test_greater():
    num = 200
    assert  num > 100

@pytest.mark.great
def test_greater_equal():
    num = 10
    assert num >=10

@pytest.mark.others
def test_less():
    num = 777
    assert  num < 999


