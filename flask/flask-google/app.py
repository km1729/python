from flask import Flask, render_template, request
import google_keyword

# create object instance
app = Flask(__name__)

@app.route('/',methods=('GET', 'POST')) # 접속하는 url
def index():
    # url에서 keyworkd1 과 keyword2에 해당하는 값 읽어옴
    # e.g. localhost:5000/?keyword1=cat&&keyword2=dog
    key1 = request.args.get('keyword1')
    key2 = request.args.get('keyword2')
    print(f'The keywords in url {key1}, {key2}')

    val1 = google_keyword.get_search_count(key1)
    val2 = google_keyword.get_search_count(key2)
    print(val1, val2)

    data = {key1:val1, key2:val2}

    # 키워드 가 none일 경우는 아무것도 하지 않기
    # 키워드 가 있을 경우 검색하기

    if key1 is None and key2 is None:
        return render_template('index.html')
    return render_template('index.html', data=data)


if __name__=="__main__":
    app.run(debug=True)