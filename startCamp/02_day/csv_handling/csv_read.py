# 1. split 함수 이용

# with open('dinner.csv','r',encoding='utf-8') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line.strip().split(",")) # csv는 항상 개행문자까지 프린드 해준다! 그러므로 지운다. 어떻게?  strip()함수를 이용해서!
#         # .split(',')를 이용하여 콤마를 기준으로 원소를 나눈다.

# 2. csv reader 사용

import csv

with open('dinner.csv', 'r', encoding='utf-8') as f:
    items = csv.reader(f)
    for item in items :
        print(item)