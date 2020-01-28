from flask import Flask, request, jsonify
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
guides_schema = GuideSchema(many=True)   # Schema is a formatting tool from marshmallow. They act as templates for database structure


# Endpoint to create a new guide
@app.route('/guide', methods=['POST'])
def add_guide():
    title = request.json['title']
    content = request.json['content']
    
    new_guide = Guide(title, content)
    
    db.session.add(new_guide)
    db.session.commit()
    
    guide = Guide.query.get(new_guide.id) 

    return guide_schema.jsonify(guide)

# endpoint to query all guides
@app.route('/guides', methods=['GET'])
def get_guides():
    all_guides = Guide.query.all()
    result = guides_schema.dump(all_guides)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)