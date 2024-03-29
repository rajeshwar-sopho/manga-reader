from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index/<name>')
@app.route('/home/<name>')
def index(name=None):
    return render_template('index.html', name=name)