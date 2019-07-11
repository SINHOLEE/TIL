# flask review
from flask import Flask, render_template, request
import requests
app = Flask(__name__)


@app.route('/') # / => root의 의미 사용자가 요청하는 페이지
def index():
    return 'Hello World!'


@app.route('/greeting/<name>')
def greeting(name) :
    return render_template('greeting.html', name=name)


@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    age = request.args.get('age')
    return f'pong! age : {age}'


@app.route('/google')
def google():
    return render_template('google.html')


@app.route('/naver')
def naver():
    return render_template('naver.html')


@app.route('/ascii_input')
def ascii_input():
    return render_template('ascii_input.html')


@app.route('/ascii_result')
def ascii_result():
    text = request.args.get('text')
    #ascii art API를 이용하여 사용자의 input값을 변경한다.
    # requsts 모듈을 사용하자.. 왜?!
    response = requests.get(f'http://artii.herokuapp.com/make?text={text}')
    result = response.text
    return render_template('ascii_result.html',result=result)


if __name__ =='__main__':   # 임포트해서 실행하면 네임은 이름이 되고, python으로 실행하면 name이 main이 된다.
                            # 즉, 위 구문은 python으로 실행했을때만 app.run()을 실행해라라는 뜻이다.
    app.run(debug=True) # 디버그 트루가 계속 수시로 껏다 켰다 하는 것
