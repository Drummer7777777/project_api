import pytest, json
#from threading import *

@pytest.fixture(scope='module')
def data_base():
    with open('data_base.json', encoding='utf-8') as f:
        users=json.load(f)
        return(users)