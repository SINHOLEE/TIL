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


# 로또 API를 가져와서 회 차 번호와 6개의 숫자를 입력받아 결과를 확인한다.

@app.route('/lotto_input') #사용자가 입력할 수 있는 페이지만 전달
def lotto_input():
    return render_template('lotto_input.html')


@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('lotto_round')
    lotto_nums = request.args.get('nums').split(" ")
    for i in range(len(lotto_nums)) :
        lotto_nums[i] = int(i)
    print(lotto_nums)
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'

    response = requests.get(url)
    #json형식의 자료를 가져올때
    lotto_infos = response.json() # json 타입의 파일을 python dictionary 로 parsing해줘
    for key, value in lotto_infos.items() :
        print(key, type(value))
    for num in lotto_nums :
        print(type(num))
    


    
    
    return f'{lotto_round}, {lotto_nums}'


if __name__ =='__main__':   # 임포트해서 실행하면 네임은 이름이 되고, python으로 실행하면 name이 main이 된다.
                            # 즉, 위 구문은 python으로 실행했을때만 app.run()을 실행해라라는 뜻이다.
    app.run(debug=True) # 디버그 트루가 계속 수시로 껏다 켰다 하는 것
