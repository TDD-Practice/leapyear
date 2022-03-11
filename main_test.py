import pytest
from main import isLeap

def test_not_divisible_by_4():
    assert not isLeap(1997) , "should be divisible by 4"

def test_divisible_by_100_and_by_400():
    assert not isLeap(1800) , "should be divisible by 100 and by 400"
