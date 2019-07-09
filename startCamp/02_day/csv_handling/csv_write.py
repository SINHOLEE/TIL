dinners = {
    '양자강' : '02-557-4211', # 차돌짬뽕
    '김밥카페' : '02-553-3181', # 라면돈까스
    '순남시래기' : '02-508-0887' # 보쌈정식
}



# # 1. 그냥 만드는 방법 (string formating)
# with open('dinner.csv', 'w', encoding='utf-8') as f:
#     for item in dinners.items() :#  [('양자강','02-557-4221'), ('김밥카페', '02-553-3181'),('순남시래기', '02-508-0887')]로 바뀜 type <class 'dict_items'>
#         f.write(f'{item[0]},{item[1]}\n')

# 2. csv writer를 사용하는 방법

import csv

with open('dinner.csv', 'w', encoding='utf-8', newline='') as f : # 매개변수를 작성할 때(ex.encoding, newline 등) 띄어쓰기 하지 않는다.=컨밴션 
    csv_writer  = csv.writer(f) # f라는 파일에 csv를 작성하는 객체를 생성
    for item in dinners.items():
        csv_writer.writerow(item) # writerow가 뭐여

        # 이 함수 쓰면 한 줄 사이에 띄어쓰기가 들어옴 그래서 newline=''을 새로운 옵션 추가해야 제대로 작성된다.
#항상 마지막에 한 라인 놔두는 것이 컨벤션
