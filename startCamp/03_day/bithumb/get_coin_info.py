#빗썸에 있는 코인의 이름과 가격을 csv파일로 추출해서 저장하시오.
import bs4
import requests
import csv

url = 'https://www.bithumb.com/'

respone = requests.get(url)
html = respone.text

# 뷰티풀숲을 이용해 코인 이름과 가격을 각각셀렉트형식으로 뽑아주세요
soup = bs4.BeautifulSoup(html,'html.parser')
coins = soup.select('.coin_list tr td p a strong')
prices = soup.select('.sort_real')

# 질문 1 빈 리스트 변수 생성 안하고 바로 코인스라는 리스트에 옮기는 방법 없나요
coin_name_list = []

for coin in coins :
    coin_name_list.append(coin.text.strip()) # 앞 뒤에 붙은 html 문법을 삭제하고 리스트형식으로 붙여주세요

price_list = []

for price in prices :
    price_list.append(price.text) # 앞 뒤에 붙은 html 문법을 삭제하고 리스트형식으로 붙여주세요

# 질문 2 -> 원, , 없애는 작업했는데... 더 깔끔하게 하고싶어요
price_list_1 = []
for i in price_list :
    i = i.replace("원","")
    if "," in i:
        i = i.replace(",","")
    i = float(i)
    price_list_1.append(i)
    print(i) 

# 질문 3 컨트롤 f5하면 오류 뜨는 이유?
coins_dic = dict(zip(coin_name_list, price_list_1))

with open('bitthub.csv', 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)
    for item in coins_dic.items():
        csv_writer.writerow(item) # writerow가 뭐여

