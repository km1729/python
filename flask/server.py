from flask import Flask
import random

app = Flask(__name__)

topics = [
    {'id':1, 'title':'html', 'body':'html is ....'},
    {'id':2, 'title':'CSS', 'body':'CSS is ....'},
    {'id':3, 'title':'Python', 'body':'Python is ....'},
    {'id':4, 'title':'Flask', 'body':'Flask is ....'}
]

@app.route('/')
def index():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/update/{topic["id"]}/">{topic["title"]}</a></li>'

    return f'''
    <!doctype html>
    <html>
        <body>
            <h1> Hello World </h1>
            <ol>
                {liTags}
            </ol>
            <h2> Welcome </h2>
            Hello, web
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
    contents = ''
    for topic in topics:
        contents = f'{topic["body"]}'
    return f'{contents}'

app.run(debug=True)
#app.run(port=5001)