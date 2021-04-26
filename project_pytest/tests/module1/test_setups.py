import pytest

"""
This Test file contains various Test functions to validate the configuration 
values provided in the CLI. 
"""

@pytest.mark.qa
def test_if_qa_setup(get_env_cli):
    assert get_env_cli == 'qa'


@pytest.mark.dev
def test_if_dev_setup(get_env_cli):
    assert get_env_cli == 'dev'


@pytest.mark.qa
def test_qa_url(app_config):
    assert app_config == 'https://www.facebook.com/'


@pytest.mark.dev
def test_dev_url(app_config):
    assert app_config == 'https://www.google.com/'
