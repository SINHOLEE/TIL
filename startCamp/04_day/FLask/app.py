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
    # 사용자 입력 값 받기
    lotto_round = request.args.get('lotto_round')
    lotto_nums = request.args.get('nums').split(" ")
    
    # 사용자가 보낸 번호를 인트값으로 변환하기
    for i in range(len(lotto_nums)) :
        lotto_nums[i] = int(lotto_nums[i])

    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'

    response = requests.get(url)
    #json형식의 자료를 가져올때
    lotto_infos = response.json() # json 타입의 파일을 python dictionary 로 parsing해줘
    
######################################################
# #밑으로 내가했당 기분좋아
    
#     for key, value in lotto_infos.items() :
#         print(key, value)
#     for num in lotto_nums :
#         print(type(num))
#     bnus_No = lotto_infos['bnusNo']
#     print(bnus_No)
    

    # winner_list = []
    # for i in range(1,7) :
    #     winner_list.append(lotto_infos[f'drwtNo{i}'])
#     print("몇 회차 당첨번호", winner_list)
#     print('내가 선택한 번호', lotto_nums)
#     print('보너스 번호', bnus_No)
#     got_set = set(winner_list)
#     got_set.add(bnus_No) # got_set = 당첨이 끝난 7개 번호
#     num_set = set(lotto_nums) # num_set = 내가 선택한 6개 번호
#     print(got_set) 
#     print(num_set)    
#     count = 0
#     for i in got_set :
#         if i in num_set :
#             count += 1
#         else:
#             pass

    
#     if count == 6 and (bnus_No not in num_set) :
#         final = "축하합니다 1등입니다."
#     elif count == 6 and (bnus_No in num_set) :
#         final = '축하합니다 2등입니다.'
#     elif count == 5 :
#         final = '축하합니다 3등입니다.'
#     elif count == 4 :
#         final = '축하합니다 4등입니다.'
#     else :
#         final = '아쉽지만 다음 기회에'
    
   
    # print(final)
    ######################################################
    # 명언 - 사용자가 준 인풋값을 믿지 말자!
    # 강사님이 짜신 로직


 

    # 보너스를 제외한 번호 뽑기
    winner_list = []
    for i in range(1,7) :
        winner_list.append(lotto_infos[f'drwtNo{i}'])    
    
    print(lotto_nums)    # 사용자가 보낸 정보
    print(winner_list)   # 보너스 제외한 당첨 번호    
    
    #번호 교집합 개수 찾기
    matched = 0
    if len(lotto_nums) == 6 :       # 사용자 숫자가 딱 6개가 맞는지 확인!!! 사용자가 준 인풋값을 믿지 않음
        for num in lotto_nums :
            if num in winner_list :
                matched += 1
    
    
        if matched == 6 :
            result = '1등입니다.'
        elif matched == 5:
            if lotto_infos['bnusNo'] in lotto_nums :
                result = '2등'
            else :
                result = '3등'
        elif matched == 4:
            result = '4등'
        elif matched == 5:
            result = '5등'
        else :
            result = '꽝'
    else :
        result = '입력한 숫자가 6개가 아닙니다.'

    print(matched)    
    # # return render_template('lotto_output.html', lotto_round=lotto_round, lotto_nums=lotto_nums, final=final, winner_list=winner_list, bnus_No=bnus_No,count=count) 
  
    return f'{lotto_round}회차, 당첨번호 는{lotto_nums} 입니다. {result} '


if __name__ =='__main__':   # 임포트해서 실행하면 네임은 이름이 되고, python으로 실행하면 name이 main이 된다.
                            # 즉, 위 구문은 python으로 실행했을때만 app.run()을 실행해라라는 뜻이다.
    app.run(debug=True) # 디버그 트루가 계속 수시로 껏다 켰다 하는 것
