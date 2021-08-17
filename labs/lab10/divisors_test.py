from divisors import divisors
from hypothesis import given, strategies
import pytest

def test_12():
    assert divisors(12) == {1,2,3,4,6,12}

@given(strategies.one_of(strategies.integers(max_value=0), strategies.characters(), strategies.decimals(), strategies.dates()))
def test_error(num):
    # If this random number is less than 0, expect it to give us a value error
    # when we want to check if an item/object is of a certain type - isinstance()
    
    with pytest.raises(ValueError):
        divisors(num)
    
@given(strategies.integers(min_value = 1, max_value=100))
def test_success(num):
    result = divisors(num)
    assert num in result
    assert 1 in result

def check_success(num, divisors):
    for item in divisors:
        if num % item != 0:
            return False
    return True


@given(strategies.integers(min_value = 1, max_value=100))
def test_results(num):
    assert check_success(num, divisors(num))

def test_empty():
    with pytest.raises(ValueError):
        divisors(None)

