# This is to setup a local host server

from flask import Flask

app = Flask(__name__)

# now you need to create a "route" using a decorator"

@app.route('/')
def hello():
    return 'Hey flask'


if __name__ == '__main__':
    app.run(debug=True)