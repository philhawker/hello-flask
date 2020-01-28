# Flask App

Basic steps to import flask and spool up a local hosted environment. 

Full CRUD functionality

### INSTALLING FLASK AND ITS DEPENDENCIES
```
pipenv install flask
pipenv install Flask-SQLAlchemy
pipenv install flask-marshmallow
pipenv install marshmallow-sqlalchemy
```

### TO IMPORT TO APP.PY
```
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
```

### TO CREATE THE DATABASE FILE
in python repl:
```
$ from app import db
$ db.create_all()
```
this will create a app.sqlite file, which is the database file


### HOW TO RUN QUERIES
Post a guide
```
Route: localhost:5000/guide
Method: POST
Body: 
{
    "title": "new title",
    "content": "my new content"
}
Content-type: JSON
```

Get all guides
```
Route: localhost:5000/guides
Method: GET
```

Get a single guide
```
id is dynamic. input desired at the end of html route (localhost:5000/guide/<id>)
Method: PUT
```

Delete a single guide
```
