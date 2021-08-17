import pytest
from decorator import add_messages, get_messages

def test_functionality():
    auth_token = 'CrocodileLikesStrawberries'
    add_messages(auth_token, 'Hi')
    add_messages(auth_token, 'I')
    add_messages(auth_token, 'Test')
    assert get_messages(auth_token) == ['Hi', 'I', 'Test']

def test_exception():
    auth_token = 'Nope'
    with pytest.raises(Exception):
        add_messages(auth_token, 'Hi')
        