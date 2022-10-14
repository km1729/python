from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!doctype html>
    <html>
        <body>
            <h1> Hello World </h1>
            <ol>
                <li><a href="/update/1/">html</a> </li>
                <li><a href="/update/2/">CSS</a> </li>
                <li><a href="/update/3/">Python</a> </li>
                <li><a href="/update/4/">Flask</a> </li>
            </ol>
        </body>
    </html>    
    '''

@app.route('/read')
def read():
    return 'read page'

@app.route('/create')
def create():
    return 'create page'

@app.route('/update/<id>/')
def update(id):
    print(id)
    return 'update ' + id

app.run(debug=True)
#app.run(port=5001)