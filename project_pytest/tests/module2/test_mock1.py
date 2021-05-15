import json

import pytest

import sys,os
sys.path.append(os.getcwd())

"""
This test uses MonkeyPatching to Test the src users.py functions,
where we mock get_user_followers with substitute_func so that there is no 
Real call to URL in get_user_followers function. 
"""


def substitute_func(username):
    my_dict = dict(username='dummy')
    return json.dumps(my_dict)


@pytest.fixture(autouse=True)
def my_mock(monkeypatch):
    from src import users
    monkeypatch.setattr(users, 'get_user_followers', substitute_func)


def test_get_follower_names_returns_name_list():
    from src.users import get_user_followers
    assert 'dummy' in json.loads(get_user_followers('username')).values()
