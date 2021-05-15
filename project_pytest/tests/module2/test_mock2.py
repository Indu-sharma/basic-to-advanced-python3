import json

import pytest
import sys,os
sys.path.append(os.getcwd())


"""
This test uses MonkeyPatching to Test the src users.py functions,
where we mock get_user_followers with substitute_func so that there is no 
Real call to URL in get_user_followers function. 
"""


def fake_get_user_followers():
    my_dict = {'user': 'Indu'}
    return json.dumps(my_dict)


@pytest.fixture
def patch(monkeypatch):
    from src import users
    monkeypatch.setattr(users, 'get_user_followers', fake_get_user_followers)


def test_get_user_followers(patch):
    from src import users
    assert users.get_user_followers() == json.dumps({'user': 'Indu'})

