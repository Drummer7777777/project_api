import pytest, requests, re, datetime, json
#from users_copy import users

#with open('data_base.json', encoding='utf-8') as f:
#        users=str(json.load(f))

passed='Passed'
failed='Failed'
not_found='Not found'

def logs(func_name, status, error=None):
    with open('tests.log', 'a+', encoding='utf-8') as f1:
        line=f'{func_name}, {status}, {error}'
        f1.writelines(line)

class TestUsers():
    #проверяем то что у юзеров валидные по формату даты
    def test_date(self):
        func_name=TestUsers.test_date.__name__
        r=requests.get('http://127.0.0.1:8080/users').text
        r=re.split(r'}, {', r)
        for data in range(len(r)):
            date = re.compile(r'\d{4}(-\d\d){2} (\d\d:){2}\d\d')
            if date.search(r[data]):
                logs(func_name, passed)
            else:
                logs(func_name, failed, 'Not found \d{4}(-\d\d){2} (\d\d:){2}\d\d')
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

    #проверяем то что по запросу приходит соответствующая инфа
    def test_users(self, data_base):
        #func_name=test_users.__name__
        r=requests.get('http://127.0.0.1:8080/users').text
        #r=re.split(r'}, {', r)
        #r=re.sub(r'\"\\n','',r)
        #r=r.replace('\n','')
        #r=re.findall(r'\[(.+)\]',r)
        print(r)
        #print(users)
        assert r=="[{'username': 'Alexeev', 'email': 'alexeev@mail.com', 'department': 'economic', 'date_joined': '2020-07-01 10:00:00'}, {'username': 'Belousov', 'email': 'belousov@mail.com', 'department': 'quality engineer', 'date_joined': '2021-07-01 10:00:00'}, {'username': 'Alexeevich', 'email': 'alexeevich@mail.com', 'department': 'manager', 'date_joined': '2022-07-01 10:00:00'}, {'username': 'Ivanov', 'email': 'alexeev@mail.com', 'department': 'quality control', 'date_joined': '2023-07-01 10:00:00'}, {'username': 'Ivanov', 'email': 'alexeev@mail.com', 'department': 'manager', 'date_joined': '2024-07-01 10:00:00'}]"

    #проверяем то что по запросу в прешедшей инфе у юзеров username содержит Alex
    def test_users_username(self):
        func_name=TestUsers.test_users_username.__name__
        r=requests.get('http://127.0.0.1:8080/users?username=Alex').text
        r=re.split(r'}, {', r)
        for data in range(len(r)):
            res = re.findall(r'.+username\': \'(.+)?\'', r[data])
            if 'Alex' in str(res):
                logs(func_name, passed)
            else:
                logs(func_name, failed, 'Alex not in res')
            assert 'Alex' in str(res)
    
    #проверяем то что по запросу отображается вся инфа из бд
    #def test_users_username_all(self):
    #    r=requests.get('http://127.0.0.1:8080/users?username=Alex').text
        

    #проверяем то что по запросу в прешедшей инфе у юзеров department содержит qual
    def test_users_department(self):
        #func_name=test_users_department.__name__
        r=requests.get('http://127.0.0.1:8080/users?department=qual').text
        r=re.split(r'}, {', r)
        for data in range(len(r)):
            res = re.findall(r'.+department\': \'(.+)?\'', r[data])
            assert 'qual' in str(res)

    #проверяем то что по запросу в прешедшей инфе у юзеров username содержит ov и department содержит qual
    def test_users_username_department(self):
        #func_name=test_users_username_department.__name__
        r=requests.get('http://127.0.0.1:8080/users?username=ov&department=qual').text
        r=re.split(r'}, {', r)
        for data in range(len(r)):
            name=re.findall(r'.+username\': \'(.+)?\'', r[data])
            res = re.findall(r'.+department\': \'(.+)?\'', r[data])
            assert 'ov' in str(name) and 'qual' in str(res)


    #def test_department(self):
    #    r=requests.get('http://127.0.0.1:8080/departments').text
    #    #r=re.split(r',', r)
    #    #pat=re.compile(r'(.+)')
    #    deprep=[]
    #    for data in range(1,len(users)):
    #        if users[str(data)]['department'] not in deprep:
    #            deprep.append(users[str(data)]['department'])
    #    assert deprep==r
    #    #dep_replay=[]
    #    #for data in range(len(r)):
    #    #        res=re.findall(pat,r[data])
    #    #        dep_replay.append(res)
    #    #assert deprep==dep_replay
                
    #проверяем то что по запросу в прешедшей инфе у департаментов name содержит qual
    def test_department_name(self):
        #func_name=test_department_name.__name__
        r=requests.get('http://127.0.0.1:8080/departments?name=qual').text
        r=re.split(r',', r)
        for data in range(len(r)):
            #res = re.findall(r'.+department\': \'(.+)?\'', r[data])
            assert 'qual' in str(r[data])