import pytest, requests, users, threading

class TestUsers():
    def test_users_list(self,start_server):
        r=requests.get('http://127.0.0.1:8080/users').text
        assert r=="[{'username': 'Alexeev', 'email': 'alexeev@mail.com', 'department': {'name': 'economic'}, 'date_joined': '2019-07-01 10:00:00'}, {'username': 'Belousov', 'email': 'belousov@mail.com', 'department': {'name': 'quality engineer'}, 'date_joined': '2019-07-01 10:00:00'}, {'username': 'Alexeevich', 'email': 'alexeevich@mail.com', 'department': {'name': 'manager'}, 'date_joined': '2019-07-01 10:00:00'}, {'username': 'Ivanov', 'email': 'alexeev@mail.com', 'department': {'name': 'quality control'}, 'date_joined': '2019-07-01 10:00:00'}, {'username': 'Ivanov', 'email': 'alexeev@mail.com', 'department': {'name': 'quality control'}, 'date_joined': '2019-07-01 10:00:00'}]"