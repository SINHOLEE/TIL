## 4일차 flask

로그인을 한다고 생각해보자.

1. 로그인  페이지가 있다.
2. 아이디와 비밀번호르 적는다.
3. 아이디와 비밀번호정보가 호스트로 넘어간다.
4. 호스트는 정보가 맞는지 확인하고 맞을 경우 우리에게 다시 로그인 정보를 보내준다.

여기서 필요한 것은 이러한 정보의 교류에 필요한 **<u>경로</u>**가 필요하다.



### 실습

우리가 필요한 route는 총 두개이다.

1. 로그인 정보를 입력할 창 (ping)
2. 로그인 후 정보를 보여줄 창(pong)

필요한 것

1. 정보를 적을 수 있는 공간.

```python
@app.route('/ping')
def ping():
    return render_template('ping.html')
```

어떤 정보를 받아올 수 있는 핑이라는 html을 생성해보자.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Ping</title>

</head>
<body>
    <form action="/pong"> # 요청하라.
        <input type="text" name="age">
        <button type="submit"> 제출하기</button>
    </form>
</body>
</html>
```

!+tap을 이용하여 기본 폼을 생성하고

action - "/pong"이라는 공간에 아래 정보를 보내라

input - name = input() 똑같다.

button - summit이라는 역할을 하는 버튼을 만든다.







그렇다면 사용자가 보낸 요청을 확인하는 객체가 필요하다

2. 정보를 어디론가 보내라고 명령하는?공간 

```python
from flask import request


@app.route('/pong')
def pong():
    age = request.args.get('age')
    return f'pong! age : {age}'

```

