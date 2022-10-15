from flask import Flask, request, redirect
import random

app = Flask(__name__)

nextId=5
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
            <h1> <a href="/">Hello World</a> </h1>
            <ol>
                {contents}
            </ol>
            <h2> Welcome </h2>
            <p>{content}</p>
            <p><a href="/create/">create</a></p>
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

@app.route('/create/', methods=['POST','GET'])
def create():
    print(request.method)
    if request.method == 'GET':
        content = '''
        <form action = "/create/" method="POST" >
            <p><input type="text" name="title"></p>
            <p><textarea name="body"></textarea></p>
            <p><input type="submit" value="create"></p>
        </form>
        '''
        return template(getContents(), content)
    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        body = request.form['body']
        newTopic = {'id':nextId , 'title':title, 'body': body}
        topics.append(newTopic)
        url = '/read/' + str(nextId) + '/'
        nextId +=1
        return redirect(url)



app.run(debug=True)
#app.run(port=5001)