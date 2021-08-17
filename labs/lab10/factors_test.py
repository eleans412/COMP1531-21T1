from factors import factors, is_prime
from hypothesis import given, strategies
import inspect
import pytest

def test_generator():
    '''
    Ensure it is generator function
    '''
    assert inspect.isgeneratorfunction(factors), "factors does not appear to be a generator"

@given(strategies.one_of(strategies.integers(max_value=1)))
def test_error(item):
    with pytest.raises(ValueError):
        list(factors(item))

@given(strategies.integers(min_value=2, max_value=100))
def test_success(item):
    mul_check = 1
    for fact in factors(item):
        mul_check *= fact
    assert mul_check == item

@given(strategies.integers(min_value=2, max_value=100))
def test_order(item):
    prev = None
    for fact in factors(item):
        if prev:
            assert fact >= prev
        prev = fact

@given(strategies.integers(min_value=2, max_value=20000))
def test_prime(item):
    for fact in factors(item):
        assert is_prime(fact)