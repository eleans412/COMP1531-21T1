from permutations import permutations
from hypothesis import given, strategies, assume

def test_base():
    assert permutations('ABC') == {'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'}

@given(strategies.text(min_size=1, max_size=5))
def test_success(string):
    for p in permutations(string):
        assert sorted(p) == sorted(string)

