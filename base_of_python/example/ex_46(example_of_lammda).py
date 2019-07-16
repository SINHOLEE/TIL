# 문제 "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"와
# 같은 문자열이 주어지고, A는 4점, B는 3점, C는 2점, D는 1점이라고 할 때 문자열에 사용된
# 알파벳 점수의 총합을 map 함수와 람다식을 이용해 구하십시오.

# 처음 내가 짠 코드
a = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"

list1 = list(a)


def choose_score(x):
    if x == "A":
        x = 4
    elif x == "B":
        x = 3
    elif x == "C":
        x = 2
    elif x == "D":
        x = 1
    return int(x)

num_list = list(map(choose_score,list1))
total = 0

v = []
for i in num_list :
    total += i
print(total)

# 람다를 사용해야 하는 조건을 부합한 코드
a = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
list1 = list(a)


c = list(map(lambda x: 4 if x == "A" else(3 if x == "B" else(2 if x == "C" else 1)),list1))


total = 0
for i in c:
    total += i
print(total)
