<div align='center'>
  <h1>project_api</h1>
</div>

## What is project_api?

project_api is api server app and tests for him written in python v3.9 It is possible ti run it all in containers Docker-compose 

### api server

Uses python lib cherrypy. Database is json file.

Before using use command 

```pip install cherrypy```

For start server use command

`python users.py`

### tests

Uses python lib pytest. Database is json file.

Before using use command 

`pip install pytest`

`pip install pytest-xdist`

For start tests should be launched server and use comand

`pytest -v -n 2 test_example.py`

###Docker-compose

For start server and tests project_api in containers use command:

`docker-compose up`

And follow link <http://127.0.0.1:8080/users>


