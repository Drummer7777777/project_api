import pytest, requests, re, datetime
from users_copy import users

class TestUsers():
    def test_date(self):
        r=requests.get('http://127.0.0.1:8080/users').text
        r=re.split(r'}, {', r)
        for data in range(len(r)):
            date = re.compile(r'\d{4}(-\d\d){2} (\d\d:){2}\d\d')
            assert date.search(r[data])
            #res = re.findall(r'.+date_joined\': \'(.+)\'', r[data])
            #assert datetime.datetime.strptime(str(res[0]), '%Y-%m-%d %H:%M:%S') == True
    
    #def test_department(self):
    #    r=requests.get('http://127.0.0.1:8080/users?department=qual').text
    #    r=re.split(r'}, {', r)
    #    list_deps=[]
    #    for data in range(len(r)):
    #        pat=re.compile(r'.+department\': \'(.+)\'')
    #        dep = pat.search(r[data])
    #        for deps in range(len(users)):
    #            if users[f'{deps}']['department'] not in list_deps:
    #                list_deps.append(users[deps]['department'])
    #        assert dep in list_deps

    def test_users(self):
        r=requests.get('http://127.0.0.1:8080/users').text
        #r=re.split(r'}, {', r)
        assert r=="[{'username': 'Alexeev', 'email': 'alexeev@mail.com', 'department': 'economic', 'date_joined': '2020-07-01 10:00:00'}, {'username': 'Belousov', 'email': 'belousov@mail.com', 'department': 'quality engineer', 'date_joined': '2021-07-01 10:00:00'}, {'username': 'Alexeevich', 'email': 'alexeevich@mail.com', 'department': 'manager', 'date_joined': '2022-07-01 10:00:00'}, {'username': 'Ivanov', 'email': 'alexeev@mail.com', 'department': 'quality control', 'date_joined': '2023-07-01 10:00:00'}, {'username': 'Ivanov', 'email': 'alexeev@mail.com', 'department': 'quality control', 'date_joined': '2024-07-01 10:00:00'}]"

    def test_users_username(self):
        r=requests.get('http://127.0.0.1:8080/users?username=Alex').text
        r=re.split(r'}, {', r)
        for data in range(len(r)):
            res = re.findall(r'.+username\': \'(.+)?\'', r[data])
            assert 'Alex' in str(res)

    def test_users_department(self):
        r=requests.get('http://127.0.0.1:8080/users?department=qual').text
        r=re.split(r'}, {', r)
        for data in range(len(r)):
            res = re.findall(r'.+department\': \'(.+)?\'', r[data])
            assert 'qual' in str(res)

    def test_department(self):
        r=requests.get('http://127.0.0.1:8080/departments').text
        r=re.split(r',', r)
        pat=re.compile(r'\'(.+)\'')
        deprep=[]
        for data in range(1,len(users)):
            if users[str(data)]['department'] not in deprep:
                deprep.append(users[str(data)]['department'])
        dep_replay=[]
        for data in range(len(r)):
                res=re.findall(pat,r[data])
                dep_replay.append(str(res))
        assert deprep==dep_replay
                

    def test_department_name(self):
        r=requests.get('http://127.0.0.1:8080/departments?name=qual').text
        r=re.split(r',', r)
        for data in range(len(r)):
            #res = re.findall(r'.+department\': \'(.+)?\'', r[data])
            assert 'qual' in str(r[data])