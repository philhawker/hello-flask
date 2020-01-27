# This is to setup a local host server

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow    # This library creates structure to the database
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
ma = Marshmallow(app)
db = SQLAlchemy(app)    # This is instantiating the SQLAlchemy and Marshmallow library to be used later


# This is building and assigning the key value pairs, or database layout or format, within the database

class Guide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False)
    content = db.Column(db.String(144), unique=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content
        
class GuideSchema(ma.Schema):
    class Meta:
        fields = ('title', 'content')
        
guide_schema = GuideSchema()
guides_schema = GuideSchema(many=True)


if __name__ == '__main__':
    app.run(debug=True)