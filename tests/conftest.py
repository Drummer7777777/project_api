import pytest, json

@pytest.fixture(scope='function')
def data_base():
    f=open('data_base.json', encoding='utf-8')
    global users
    users=json.load(f)
    print(users)
    yield users
    f.close()
