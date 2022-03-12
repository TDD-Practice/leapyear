import pytest
from main import isLeap

def test_divisible_by_4():
    assert not isLeap(1997) , "should be divisible by 4"
    assert isLeap(1996) , "should be leap"

def test_divisible_by_100_and_by_400():
    assert not isLeap(1800) , "should be divisible by 100 and by 400"
    assert isLeap(1600) , "should be leap"
