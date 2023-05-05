import pytest
from Class26 import *


def test_addition_positive():
    result = addition(3, 4)
    assert result == 7


def test_addition_negative():
    result = addition(-3, -4)
    assert result == -7


def test_addition_positive_negative():
    result = addition(-3, 4)
    assert result == 1


def test_addition_decimals():
    result = addition(2.4, 4.5)
    assert result == 6.9


@pytest.mark.skip
def test_addition_numeric_decimals():
    result = addition(2, 4.5)
    assert result == 6.5

@pytest.mark.xfail
def test_addition_decimals1():
    result = addition(2.4, 4.5)
    assert result == 5
