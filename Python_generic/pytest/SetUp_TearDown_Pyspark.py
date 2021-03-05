import pytest
import elasticsearch as ES


@pytest.fixture(scope="module")
def myconn(es="192.168.1.1:9200"):
    my_es = ES(es)
    yield my_es
    my_es.close()

@pytest.mark.elastic
def test_getindex(myconn):
    index = myconn.func_name
    assert index == "xyz"
