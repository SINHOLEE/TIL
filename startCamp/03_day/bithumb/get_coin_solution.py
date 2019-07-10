import requests
import bs4
import csv

#1. 빗섬 페이지를 가지고 온다.
response = requests.get('https://www.bithumb.com/')

# 요청을 보내 응답을 받는지 확인 한다 : <Response [200]> 라면 성공적으로 받아옴
# print(response)

html = response.text # 응답박은 객체에서 html 문서를 string으로 가져 옴

# 타입을 확인하면 <class 'str'> 형식이라고 나온다. 
# print(type(html)) 

# 2 그렇기 때문에 beautifulsoup모듈을 이용하여 string type의 html 을 파싱한다.
soup = bs4.BeautifulSoup(html, 'html.parser')

# 3 각각의 코인정보를 가지고 있는 tr를 리스트 형식으로 받아오겠다.
# 'coin_list' 안에 있는 'tr'에 리스트형식으로 모두 가져와 주세요
# css 문법 1. '.coin_list tr' => 코인리스트 안에 tr을 가져올게요 는 띄어쓰기로 표현
# css 문법 2. . 은 클래스에 접근할때 쓰는 문법
coins = soup.select('.coin_list tr') 

# 프린트를 해보면 어지럽지만 결국 리스트형식으로 받아온 것을 안다. 
# print(coins)

# 4 각 코인을 순회하며 필요한 정보만 추출한다.
for coin in coins :
    # 각 코인의 이름과 시세 데이터를 추출 
    # tableAsset > tbody > tr:nth-child(1) > 여기까지가 coin이라는 뜻
    # td:nth-child(1) 
    coin_name = coin.select_one('td:nth-child(1) > p > a > strong').text.replace('NEW', '')
    coin_price = coin.select_one('td:nth-child(2) > strong').text.replace("원","")
    coin_price = coin_price.replace(",","")

# 5 csv writer로 csv파일을 만들자

with open('coin_solution.csv','w',encoding='utf-8', newline='') as f :
    csv_writer = csv.writer(f)
    # 6  # 4를 with open 안으로 가져온다.
    for coin in coins :
        coin_name = coin.select_one('td:nth-child(1) > p > a > strong').text.replace('NEW', '').strip()
        coin_price = coin.select_one('td:nth-child(2) > strong').text.replace("원","")
        coin_price = coin_price.replace(",","")
        data = (coin_name, coin_price)
        print(data)
        csv_writer.writerow(data)