import requests
from number_fun import multiply_by_two, print_message, sum_list_of_numbers, sum_iterable_of_numbers, is_in, index_of_number
import config

BASE_URL = ''

def test_multiply():
    data = {'number' : 2}

    resp1 = requests.get(config.url + '/multiply', params=data)
    load = resp1.json()
    assert resp1.status_code == 200
    assert load == 4 

def test_message():
    data = {'message' : 'hello world'}
    resp1 = requests.get(config.url + '/message', params=data)
    
    load = resp1.json()

    assert load == 'hello world'


def test_sum():
    data = {'numbers' : [1,2,3,4,5]}
    resp1 = requests.get(config.url + '/sum', params=data)
    assert resp1.status_code == 200

    load = resp1.json()
    assert load == 15

def test_find_num():
    data = {'needle' : 2,'haystack' : [1,2,3,4,5]}
    resp1 = requests.get(config.url + '/search', params=data)
    assert resp1.status_code == 200
    load = resp1.json()
    assert load

def test_index():
    data = {'item' : 3, 'numbers' : [1,2,3,4,5]}
    resp1 = requests.get(config.url + '/search_idx', params=data)
    assert resp1.status_code == 200
    load = resp1.json()
    assert load == 2
