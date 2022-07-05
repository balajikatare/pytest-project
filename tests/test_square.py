import math

global num
num = 25
def test_sqrt():
    assert  math.sqrt(num) == 5



def testsquare():
    global num
    num = 7
    assert  7*7 == 40


def testquality():
    assert  10 == 100
