import cherrypy, json

with open('data_base.json', encoding='utf-8') as f:
        users=json.load(f)

def main():
    
    class Users:
        def GET(self, username=None, department=None):
            data,data2,data3 = {},{},{}
            if username==None:
                for idd in users:
                    data[idd]=users[idd]#['username'])
                    #add=str(idd)+': '+str(users[idd])
                    #data.append(add)#['username'])
            else:
                for idd in users:
                    if username in users[idd]['username']:
                        data[idd]=users[idd]#['username'])
            if department==None:
                for idd in users:
                    data2[idd]=users[idd]#['username'])
            else:
                for idd in users:
                    if department in users[idd]['department']:
                        data2[idd]=users[idd]#['username'])
            for item in data:
                if item in data2:
                    data3[item]=users[item]
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