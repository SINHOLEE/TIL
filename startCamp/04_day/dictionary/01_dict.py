# 딕셔너리 생성
lunch1 = {
    '중국집' : '02'
    
}

#또 다른 딕셔너리 만드는 방법
lunch2 = dict(중국집='02') 

print(lunch1)
print(lunch2)

#딕셔너리 내용 추가하기
lunch1['중국집'] #'02'
lunch1['분식집'] = '031'

#딕셔너리 내용 가져오기
idol = {
    'BTS' : {
        '지민' : 24,
        'RM' : 25,
    }
}

print(idol['BTS']['RM'])

print('-'*25)
#딕셔너리 반복문 활용하기

# 기본활용
for key in lunch1 :
    print(key, lunch1[key])

# value만 가져오기
for value in lunch1.values():
    print(value)

# key만 가져오기
for key in lunch1.keys():
    print(key)

# .items() => key, value 가져오기
for key, value in lunch1.items():
    print(key, value)
print(lunch1.items()) # [('중국집','02')('분식집','031')]