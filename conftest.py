import pytest, users, time
from threading import *

@pytest.fixture(scope='session')
def start_server():
    t1 = Thread(target = users.main())
    t1.start()
    time.sleep(3)
    yield start_server
    users.exit()