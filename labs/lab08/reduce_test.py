from reduce import reduce

def test_functionality():
    assert reduce(lambda x, y: x + y, [1,2,3,4,5]) == 15
    assert reduce(lambda x, y: x + y, [1]) == 1
    assert reduce(lambda x, y: x + y, []) == None

