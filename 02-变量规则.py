from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/hello/<username>')
def hello(username):
    return f'Hello {username}!'


@app.route('/integer/<int:id>')
def show_integer(id):
    return f'Integer: {id}'


@app.route('/path/<path:path>')
def show_path(path):
    return f'path: {escape(path)}'


if __name__ == '__main__':
    app.run(debug=True)
