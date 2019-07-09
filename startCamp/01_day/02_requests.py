import requests
import bs4 # 받은 문서를 이쁘게 만들어 주세요


url = 'https://finance.naver.com/sise/'

response = requests.get(url) # 리퀘스트 겟함수를 이용하여 응답을 받고.
html = response.text        # 응답받은 리스폰변수에 .text하면 글자로 보내줘

soup = bs4.BeautifulSoup(html, 'html.parser') # 우리가 읽기 쉽게 파싱해줘(접근하기 쉽게 만들어줘. 변환해줘?)
kospi = soup.select_one('#KOSPI_now') #파싱을 했기 때문에 셀렉트 원 함수로 접근 가능하게 됨 / 아이디값은 #으로 접근

print(kospi.text)

#user-content-wrapper


print(response)
print(response.status_code) # 스테이터스 코드란? 잘 받았으면 200, 잘 안되었으면 404 나중에 다시 배우자

# bs4 공부 
#.select(selector) -> 셀렉터의 내용을 전부? 뽑아줘,,.?
#.select_one(selector) -> 셀렉터의 내용 하나만 뽑아줘