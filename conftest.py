import pytest, json
#from threading import *

@pytest.fixture(scope='class')
def data_base():
    f=open('data_base.json', encoding='utf-8')
    global users
    users=json.load(f)
    print(users)
    return data_base
    yield
    f.close()