import re

st="[{'username': 'Alexeev', 'email': 'alexeev@mail.com', 'department': {'name': 'economic'}, 'date_joined': '2019-07-01 10:00:00'}, {'username': 'Belousov', 'email': 'belousov@mail.com', 'department': {'name': 'quality engineer'}, 'date_joined': '2020-07-01 10:00:00'}, {'username': 'Alexeevich', 'email': 'alexeevich@mail.com', 'department': {'name': 'manager'}, 'date_joined': '2021-07-01 10:00:00'}, {'username': 'Ivanov', 'email': 'alexeev@mail.com', 'department': {'name': 'quality control'}, 'date_joined': '2022-07-01 10:00:00'}, {'username': 'Ivanov', 'email': 'alexeev@mail.com', 'department': {'name': 'quality control'}, 'date_joined': '2023-07-01 10:00:00'}]"
#result = re.split(r',', st)
resul=re.split(r'}, {', st)
#print(resul[1])
#print(len(resul))
for data in range(len(resul)):
    res = re.findall(r'.+date_joined\': \'(.+)\'', resul[data])
    print(str(res[0]))