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
