import pytest
global a
@pytest.fixture()
def setUp():
    global a
    a = 1
    return 1

def test_Case1(setUp):
    assert a == 1, "Error message"
