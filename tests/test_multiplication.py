import pytest


@pytest.mark.parametrize("num, output", [(1, 11), (2, 22), (3, 33), (4, 44)])
def test_multiplication(num, output):
    assert 11 * num == output


@pytest.mark.parametrize("num,square_root", [(4, 2), (9, 3), [16, 4], [25, 5]])
def test_square(num, square_root):
    assert num == square_root * square_root, "{} is not square root of  {}".format(square_root, num)

