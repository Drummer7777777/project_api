import pytest, requests, re, datetime

class TestUsers():
    def test_users_list(self, start_server):
        r=requests.get('http://127.0.0.1:8080/users').text
        r=re.split(r'}, {', r)
        for data in range(len(r)):
            res = re.findall(r'.+date_joined\': \'(.+)\'', r[data])
            assert datetime.datetime.strptime(str(res[0]), '%Y-%m-%d %H:%M:%S') == True