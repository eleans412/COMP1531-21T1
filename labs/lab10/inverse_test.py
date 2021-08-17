from inverse import inverse
import pytest
from hypothesis import given, strategies

def test_functionality():
    assert inverse({1: 'A', 2: 'B', 3: 'A'}) == {'A': [1, 3], 'B': [2]}
    assert inverse({3: 'L', 5: 'L', 4: 'L'}) == {'L' : [3, 5, 4]}


def test_none_input():
    with pytest.raises(ValueError):
        inverse(None)

