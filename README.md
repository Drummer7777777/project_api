<div align='center'>
  <h1>project_api</h1>
</div>

## What is project_api?

project_api is api server app and tests for him written in python v3.9

### api server

Uses python lib cherrypy. Database is json file.
Before using use command 
```pip install cherrypy```
For start server use command
`python users.py`

### tests

Uses python lib pytest. Database is json file.
For start tests should be launched server and use comand
`pytest -v -n 2 test_example.py`
