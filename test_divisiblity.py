import divisblity
import pytest

@pytest.fixture
def input():
    a = 25
    return a

def test_divby5(input):
    # a = 10
    out1 = divisblity.divby5(input)
    assert out1 == True


def test_divby5_1(input):
    # a = 14
    out1 = divisblity.divby5(input)
    assert out1 == False


def test_divby7(input):
    # a = 10
    out1 = divisblity.divby7(input)
    assert out1 == False


def test_divby7_1(input):
    # a = 14
    out1 = divisblity.divby7(input)
    assert out1 == True


def test_divby9(input):
    # a = 10
    out1 = divisblity.divby9(input)
    assert out1 == False


def test_divby9_1(input):
    # a = 18
    out1 = divisblity.divby9(input)
    assert out1 == True


def test_divby11(input):
    # a = 10
    out1 = divisblity.divby11(input)
    assert out1 == False


def test_divby11_1(input):
    # a = 121
    out1 = divisblity.divby11(input)
    assert out1 == True

