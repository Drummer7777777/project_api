import pytest, requests, re, datetime, json
#from users_copy import users

#with open('data_base.json', encoding='utf-8') as f:
#        users=json.load(f)

passed='Passed'
failed='Failed'
not_found='Not found'

def logs(func_name, status, error='Not errors'):
    with open('tests.log', 'a+', encoding='utf-8') as f1:
        line=f'{func_name}, {status}, {error}\n'
        f1.writelines(line)

class TestUsers():
    #по /users выводится весь список юзеров
    def test_users(self, data_base):
        func_name=TestUsers.test_users.__name__
        r=requests.get('http://host.docker.internal:8080/users').text
        if r==str(data_base):
            logs(func_name, passed)
        else:
            logs(func_name,failed,'Data in api doesn\'t match in database')
        assert r==str(data_base)

    #по /users?username=Alex в ответе у всех юзеров есть совпадения
#    def test_users_username(self):
#        func_name=TestUsers.test_users_username.__name__
#        r=requests.get('http://127.0.0.1:8080/users?username=Alex').text
#        r=re.split(r'}, {', r)
#        for data in range(len(r)):
#            res = re.findall(r'.+username\': \'(.+)?\'', r[data])
#            if 'Alex' in str(res):
#                logs(func_name, passed)
#            else:
#                logs(func_name, failed, 'Alex not in res')
#            assert 'Alex' in str(res)
#    
#    #по /users?username=Alex в ответе есть все совпадения
#    def test_users_username_all(self,data_base):
#        func_name=TestUsers.test_users_username_all.__name__
#        r=requests.get('http://127.0.0.1:8080/users?username=Alex').text
#        all_coincidence={}
#        for key in data_base:
#            if 'Alex' in data_base[key]['username']:
#                all_coincidence[key]=data_base[key]
#        if r==str(all_coincidence):
#            logs(func_name,passed)
#        else:
#            logs(func_name,failed,'В ответе не все совпадения')
#        assert r==str(all_coincidence)
#
#
#    #по /users?department=qual в ответе у всех юзеров есть совпадения
#    def test_users_department(self):
#        func_name=TestUsers.test_users_department.__name__
#        r=requests.get('http://127.0.0.1:8080/users?department=qual').text
#        r=re.split(r'}, {', r)
#        for data in range(len(r)):
#            res = re.findall(r'.+department\': \'(.+)?\'', r[data])
#            if 'qual' in str(res):
#                logs(func_name, passed)
#            else:
#                logs(func_name,failed,'Не найден текст фильтра в ответе')
#            assert 'qual' in str(res)
#
#    #по /users?department=qual в ответе есть все совпадения
#    def test_users_department_all(self, data_base):
#        func_name=TestUsers.test_users_department_all.__name__
#        r=requests.get('http://127.0.0.1:8080/users?department=qual').text
#        all_coincidence={}
#        for key in data_base:
#            if 'qual' in data_base[key]['department']:
#                all_coincidence[key]=data_base[key]
#        if r==str(all_coincidence):
#            logs(func_name,passed)
#        else:
#            logs(func_name,failed,'В ответе не все совпадения по department')
#        assert r==str(all_coincidence)
#
#    #по /users?username=ov&department=qual в ответе у всех юзеров есть совпадения
#    def test_users_username_department(self):
#        func_name=TestUsers.test_users_username_department.__name__
#        r=requests.get('http://127.0.0.1:8080/users?username=ov&department=qual').text
#        r=re.split(r'}, {', r)
#        for data in range(len(r)):
#            name=re.findall(r'.+username\': \'(.+)?\'', r[data])
#            res = re.findall(r'.+department\': \'(.+)?\'', r[data])
#            if 'ov' in str(name) and 'qual' in str(res):
#                logs(func_name,passed)
#            else:
#                logs(func_name,failed,'Не найден текст фильтра в ответе')
#            assert 'ov' in str(name) and 'qual' in str(res)
#    
#    #по /users?username=ov&department=qual есть все совпадения
#    def test_users_username_department_all(self, data_base):
#        func_name=TestUsers.test_users_username_department_all.__name__
#        r=requests.get('http://127.0.0.1:8080/users?username=ov&department=qual').text
#        all_coincidence={}
#        for key in data_base:
#            if ('ov' in data_base[key]['username']) and ('qual' in data_base[key]['department']):
#                all_coincidence[key]=data_base[key]
#        if r==str(all_coincidence):
#            logs(func_name,passed)
#        else:
#            logs(func_name,failed,'В ответе не все совпадения')
#        assert r==str(all_coincidence) 
#
#    #проверяем то что у юзеров валидные по формату даты
#    def test_date(self):
#        func_name=TestUsers.test_date.__name__
#        r=requests.get('http://127.0.0.1:8080/users').text
#        r=re.split(r'}, {', r)
#        for data in range(len(r)):
#            date = re.compile(r'\d{4}(-\d\d){2} (\d\d:){2}\d\d')
#            if date.search(r[data]):
#                logs(func_name, passed)
#            else:
#                logs(func_name, failed, 'Дата не соответствует формату')
#            assert date.search(r[data])
#            #res = re.findall(r'.+date_joined\': \'(.+)\'', r[data])
#            #assert datetime.datetime.strptime(str(res[0]), '%Y-%m-%d %H:%M:%S') == True
#    
#    #def test_department(self):
#    #    r=requests.get('http://127.0.0.1:8080/users?department=qual').text
#    #    r=re.split(r'}, {', r)
#    #    list_deps=[]
#    #    for data in range(len(r)):
#    #        pat=re.compile(r'.+department\': \'(.+)\'')
#    #        dep = pat.search(r[data])
#    #        for deps in range(len(users)):
#    #            if users[f'{deps}']['department'] not in list_deps:
#    #                list_deps.append(users[deps]['department'])
#    #        assert dep in list_deps
#    
#
#    
#    
#    #проверяем то что по запросу отображается вся инфа из бд
#    #def test_users_username_all(self):
#    #    r=requests.get('http://127.0.0.1:8080/users?username=Alex').text
#        
#
#    
#
#    
#
#    #по /departments в ответе есть все департаменты
#    def test_department_all(self, data_base):
#        func_name=TestUsers.test_department_all.__name__
#        r=requests.get('http://127.0.0.1:8080/departments').text
#        all_department=[]
#        for key in data_base:
#            if data_base[str(key)]['department'] not in all_department:
#                all_department.append(data_base[str(key)]['department'])
#        if r==str(all_department):
#            logs(func_name, passed)
#        else:
#            logs(func_name, failed, 'В ответе нет всех департаментов')
#        assert r==str(all_department)
#        #r=re.split(r',', r)
#        #pat=re.compile(r'(.+)')
#        #deprep=[]
#        #for data in range(1,len(users)):
#        #    if users[str(data)]['department'] not in deprep:
#        #        deprep.append(users[str(data)]['department'])
#        #assert deprep==r
#        #dep_replay=[]
#        #for data in range(len(r)):
#        #        res=re.findall(pat,r[data])
#        #        dep_replay.append(res)
#        #assert deprep==dep_replay
#    
#    #по /departments в ответе все департаменты уникальны
#    def test_department_unic(self):
#        func_name=TestUsers.test_department_unic.__name__
#        r=requests.get('http://127.0.0.1:8080/departments').text
#        rep=0
#        deps=[]
#        r=re.split(r',',r)
#        pat=re.compile(r'.*\'(.+)\'.*')
#        for item in range(len(r)):
#            dep=re.findall(pat,r[item])
#            if dep not in deps:
#                deps.append(dep)
#            else:
#                rep+=1
#        if rep==0:
#            logs(func_name, passed)
#        else:
#            logs(func_name, failed, 'В ответе повторяются значения')
#        assert rep==0 
#                
#    #по /departments?name=qual' в ответе у всех департаментов есть совпадения
#    def test_department_name(self):
#        func_name=TestUsers.test_department_name.__name__
#        r=requests.get('http://127.0.0.1:8080/departments?name=qual').text
#        r=re.split(r',', r)
#        eq=True
#        for data in range(len(r)):
#            if 'qual' not in str(r[data]):
#                eq=False
#            if eq==False:
#                logs(func_name,failed,'В ответе не у всех департаментов есть совпадения')
#            if data==len(r)-1 and eq==True:
#                logs(func_name,passed)
#            #res = re.findall(r'.+department\': \'(.+)?\'', r[data])
#            assert 'qual' in str(r[data])
#
#    #по /departments?name=qual' найдены все совпадения
#    def test_department_name_all(self, data_base):
#        func_name=TestUsers.test_department_name_all.__name__
#        r=requests.get('http://127.0.0.1:8080/departments?name=qual').text
#        all_coincidence=[]
#        for key in data_base:
#            if ('qual' in data_base[key]['department']) and (data_base[key]['department'] not in all_coincidence):
#                all_coincidence.append(data_base[key]['department'])
#        if r==str(all_coincidence):
#            logs(func_name,passed)
#        else:
#            logs(func_name,failed,'В ответе не все совпадения')
#        assert r==str(all_coincidence)