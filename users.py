import cherrypy
global users
users = {
        '1' : {
            'username' : 'Alexeev',
            'email' : 'alexeev@mail.com',
            'department' : 'economic',
            'date_joined' : '2020-07-01 10:00:00'
        },
        '2' : {
            'username' : 'Belousov',
            'email' : 'belousov@mail.com',
            'department' : 'quality engineer',
            'date_joined' : '2021-07-01 10:00:00'
        },
        '3' : {
            'username' : 'Alexeevich',
            'email' : 'alexeevich@mail.com',
            'department' : 'manager',
            'date_joined' : '2022-07-01 10:00:00'
        },
        '4' : {
            'username' : 'Ivanov',
            'email' : 'alexeev@mail.com',
            'department' : 'quality control',
            'date_joined' : '2023-07-01 10:00:00'
        },
        '5' : {
            'username' : 'Ivanov',
            'email' : 'alexeev@mail.com',
            'department' : 'quality control',
            'date_joined' : '2024-07-01 10:00:00'
        }
    }

depart : {
    'economic',
    'quality engineer',
    'manager',
    'quality control',
    'quality control'
}

def main():
    
    class Users:
        def GET(self, username=None, department=None):
            data,data2,data3 = [],[],[]
            if username==None:
                for idd in users:
                    data.append(users[idd])#['username'])
            else:
                for idd in users:
                    if username in users[idd]['username']:
                        data.append(users[idd])#['username'])
            if department==None:
                for idd in users:
                    data2.append(users[idd])#['username'])
            else:
                for idd in users:
                    if department in users[idd]['department']:
                        data2.append(users[idd])#['username'])
            for item in data:
                if item in data2:
                    data3.append(item)
            return('%s' % data3)

        exposed = True

    class Departments:
        def GET(self, name=None):
            #if department == None:
                data,data2 = [],[]
                for idd in users:
                    if users[idd]['department'] not in data:
                        data.append(users[idd]['department'])
                if name == None:
                    return ('%s' % data)
                else:
                    for i in range(len(data)):
                        if name in data[i]:
                            data2.append(data[i])
                    return ('%s' % data2)
        exposed = True

    #if __name__ == '__main__':
    cherrypy.tree.mount(
        Users(), '/users',
        {'/':
            {'request.dispatch':cherrypy.dispatch.MethodDispatcher()}
        }    
    ),
    cherrypy.tree.mount(
        Departments(), '/departments',
        {'/':
            {'request.dispatch':cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.quickstart()

def exit():
    cherrypy.engine.stop()

main()