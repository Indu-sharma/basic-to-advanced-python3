import pytest

""" 
Simple Test for using ES connection for getting the Index 
"""

@pytest.mark.elastic
def test_getindex(myconn):
    index = myconn.func_name
    assert index == "xyz"