from flask import Flask, render_template, request

# create object instance
app = Flask(__name__)

# python decorator
@app.route("/")
def index():
    return render_template('index.html',user="k",
    data={'level':60,'point':360,'exp':45000})
# def index():
#     if request.method == "POST":
#         # user=request.form['user'] # 전달받은 name이 user인 데이터
#         print(request.form.get('user')) # 안전하게 가져오려면 get
#         user = request.form.get('user')
#         data = {'level': 60, 'point': 360, 'exp': 45000}
#         return render_template('index.html', user=user, data=data)
#     elif request.method == "GET":
#         user = "반원"
#         data = {'level': 60, 'point': 360, 'exp': 45000}
#         return render_template('index.html', user=user, data=data)

# app.run(host="", port="", debug=True)
if __name__ == "__main__":
    app.run(debug=True)