import pytest
from Class26 import *


def test_subtraction_positive():
    result = subtraction(3, 4)
    assert result == -1


def test_subtraction_negative():
    result = subtraction(-3, -4)
    assert result == 1


def test_subtraction_positive_negative():
    result = subtraction(-3, 4)
    assert result == -7


def test_subtraction_decimals():
    result = subtraction(2.4, 4.5)
    assert result == -2.1


def test_subtraction_numeric_decimals():
    result = subtraction(2, 4.5)
    assert result == -2.5

