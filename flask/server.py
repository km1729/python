from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Kaycee HI'

app.run(debug=True)
#app.run(port=5001)