from flask import Flask
import random

app = Flask(__name__)

topics = [
    {'id':1, 'title':'html', 'body':'html is ....'},
    {'id':2, 'title':'CSS', 'body':'CSS is ....'},
    {'id':3, 'title':'Python', 'body':'Python is ....'},
    {'id':4, 'title':'Flask', 'body':'Flask is ....'}
]

def template(contents, content):
    return f'''
    <!doctype html>
    <html>
        <body>
            <h1> Hello World </h1>
            <ol>
                {contents}
            </ol>
            <h2> Welcome </h2>
            {content}
        </body>
    </html>    
    '''

def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags



@app.route('/')
def index():    
    return template(getContents(), '<h2>Hello World</h2>')

@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}')

@app.route('/create')
def create():
    return 'create page'



app.run(debug=True)
#app.run(port=5001)