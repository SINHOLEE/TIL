# a = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
# list1 = list(a)
# 
# 
# c = list(map(lambda x: 4 if x == "A" else(3 if x == "B" else(2 if x == "C" else 1)),list1))
# 
# 
# total = 0
# for i in c:
#     total += i
# print(total)
# 
"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')
total = 0
for i in score.values():
    total += i

avg = (total/len(score.values()))
print(avg)
# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')

# a_avg = a반 평균
# b_avg = b반 평균
# total_avg = 전체평균
total = 0
a_total = 0
b_total = 0

for score in scores :
    for i in scores[score] :
        if score == 'a':
            a_total += scores[score][i]
        elif score == 'b':
            b_total += scores[score][i]
a_avg = a_total/len(scores['a'])
b_avg = b_total/len(scores['b'])
total_avg = (a_avg +b_avg)/2
print('a반 평균은 :{0}, b반 평균은 :{1}, 전체평균은 :{2}'.format(a_avg, b_avg, total_avg))

# 선생님이 푸신 방법

print('==== Q2 ====by.teather')

total_score = 0
count = 0

for person_score in scores.values():
    total_score += sum(person_score.values())
    count += len(person_score)

average_score = total_score/count

print(average_score)


# 3. 도시별 최근 3일의 온도입니다.
cities = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
total = 0
for city in cities:
    total = sum(cities[city])
    avg = total/len(cities[city])
    print('{} : {:0.2f}'.format(city, avg))
    total = 0
print('==== Q3-1====by.teather')

for key, value in cities.items() :
    average_temp = sum(value)/len(value)
    print('{} : {}'.format(key,average_temp))





# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
list1= []
for city in cities :
    for i in cities[city] :
        list1.append(i)


hot = max(list1)
cold = min(list1)

for city in cities :
    for i in cities[city] :
        if i == hot :
            print('가장 더웠던 곳 : {0}'.format(city))
        elif i == cold :
            print('가장 추웠던 곳 : {}'.format(city))

print('==== Q3-2====by.teather')

# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
ab = 0
for city in cities :
    for i in cities[city] :
        if i == 2 and city == '서울' :
            ab = 1



if ab == 1 :
    print('예')
else:
    print('아니오')