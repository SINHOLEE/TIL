from flask import Flask, render_template
import datetime
import random

app = Flask(__name__)

@app.route('/') # 데코레이터 이름만 알고 있으면 다음에.. 역할 : 
def hello():
    # return 'Hello SadSAFY!'
    # 수시로 코드를 수정하면서 라이브 서버처럼 안돌아가.. 그래서 디버그 설정을 해야함
    return render_template('index.html')
    # 중요 1 render_templates임포트한다.
    # 중요 2 꼭 templates 폴더를 생성해야한다 꼭 app.py 파일이 있는 공간에
    # 중요 3 리턴에 꼭 위에처럼 작성해야 한다.
    # 중요 4 index.html을 ㅏㄴ들자.


@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    b_day = datetime.datetime(2019,7,27)
    td = b_day - today
    return f'{td.days} 일 남았습니다.'


@app.route('/html')
def html():
    return '<h1> This is HTML h1 tag </h1>'


@app.route('/html_lines')
def html_liness():
    return '''
    <h1> 여러줄을 보내봅시다. </h1>
    <ul>
        <li> 1번 </li>
        <li> 2번 </il>
    </ul>
    '''


# Variable Routing
@app.route('/greeting/<name>') # 이름 받기 사이트 작성
def greeting(name) :
    return render_template('greeting.html', html_name=name)


@app.route('/cube/<int:num>')
def cube(num):
    resert = num ** 3
    return render_template('cube.html', html_num=num, resert=resert)


# 실습 메뉴를 임의로 구성하고 랜덤으로 사람 수만큼 메뉴를 뽑아내도록 코드를 작성하시오.
@app.route('/lunch/<int:people>')
def people(people):
    menu = ['짜장면','탕수육', '김치볶음밥', '떡볶이']
    list = [random.choice(menu) for i in range(people)]
    list = sorted(list)
    return f'사람 수는 총 {people} 명입니다. {list}'


@app.route('/movie')
def movie():
    movies = ["알라딘", "기생충", "토이스토리4"]
    return render_template('movie.html', movies=movies)   

if __name__ =='__main__':   # 임포트해서 실행하면 네임은 이름이 되고, python으로 실행하면 name이 main이 된다.
                            # 즉, 위 구문은 python으로 실행했을때만 app.run()을 실행해라라는 뜻이다.
    app.run(debug=True) # 디버그 트루가 계속 수시로 껏다 켰다 하는 것

