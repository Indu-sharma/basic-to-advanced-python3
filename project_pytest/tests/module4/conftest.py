"""
This is Module Level conftest.py
"""
import elasticsearch as ES
import pytest

# Simple Fixture for ES connection setup and Teardown.


@pytest.fixture(scope="module")
def myconn(es="192.168.1.1:9200"):
    my_es = ES(es)
    yield my_es
    my_es.close()