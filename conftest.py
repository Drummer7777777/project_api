import pytest, users

@pytest.fixture(scope='session')
def start_server():
    users.main()
    yield start_server
    users.exit()