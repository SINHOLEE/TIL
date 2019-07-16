#2-4 5개의 숫자를 입력받아 리스트와 평균을 출력하시오
'''
num = [int(input()) for i in range(5)]

print('입력된 값 {}의 평균은 {:0.1f}입니다.'.format(num, (sum(num)/len(num))))
'''

# 2-6 정수를 입력받고 그 정수의 모든 약수를 리스트 형식으로 출력하시오
'''
num = int(input())

divisor = []
for i in range(1, (num+1)):
    if num % i == 0 :
        divisor.append(i)

print(divisor)
'''
# 2-7 다음의 결과와 같이 정수를 입력하면 리스트 내포를 이용해 약수 리스트를 출력하는 코드를 작성하십시오
'''
num = int(input())

divisor = [i for i in range(1,(num+1)) if num % i == 0]

print(divisor)
'''

# 2-8 [1, 3, 11, 15, 23, 28, 37, 52, 85, 100] 와 같은 리스트 객체가 주어졌을 때 다음의 결과를 출력하는 짝수만 항목으로 가지는 리스트 객체를 생성하는 코드를 작성하십시오.
'''
nums = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]

new_nums = []
for i in range(1, len(nums)) :
    if nums[i] % 2 == 0:
        new_nums.append(nums[i])

print(new_nums)
'''

# 2-11 리스트 내포 가능을 이용해 피보나치 수열 10번째까지 출력하는 프로그램을 작성하십시오.
'''
# 내포함수를 쓰지 않은 피보나치 수열
[1,1,2,3,5,8,13,21,34,55]

count = int(input())
i = 0
fi_bo = []
while i != count :
        if i == 0 :
                fi_bo.append(1)
        elif i == 1 :
                fi_bo.append(1)
        elif i >= 2 :
                new = fi_bo[i-2] + fi_bo[i-1]
                fi_bo.append(new)
        i += 1
print(fi_bo)
'''

'''
# 내포함수를 이용하여 작성하려 했던 구문 / 실패
fi_bo = [for i in range(1,11) if i == 1 else (if i == 2)]
'''

'''
def fibonacci(num):
    answer = [0,1]    #list의 초기값을 0,1로 지정
 
    for i in range(2,num+1):#i는 list의 주소를 뜻함
        answer.append(answer[i-1]+answer[i-2])#list에 추가하겠음
    #print(answer)  #이것은 피보나치 list를 출력해 보기 위해
    #print(i)       #이것은 리스트 주소가 잘 돌고있는지 확인하기위해
    return answer[1:]    #리스트에서 가장 마지막것만 출력해준다!
 

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(5))


출처: https://rednooby.tistory.com/74 [개발자의 취미생활]
'''

'''
# 위 자료를 참고해서 짠 코드
answer = [0, 1]
result = [answer.append(answer[i-1]+answer[i-2]) for i in range(2, 11)]

print(answer[1:])
'''
# 2-12 리스트 내포 기능을 이용하여 1부터 20사이의 숫자 중 3의 배수가 아니거나 5의 배수가 아닌 숫자들의 제곱 값으로 구성된 리스트 객체를 출력하는 프로그램을 작성하십시오.

'''
nums = [x**2 for x in range(1,21) if ( x % 3 != 0 ) or ( x % 5 != 0 )]

print(nums)
'''

# 2-13 사용자가 숫자를 입력하면 숫자의 각 자릿수의 합을 구해서 반환하는 프로그램을 작성하십시오. 예를 들어 123을 입력하면 1 + 2 + 3 = 6의 결과를 반환합니다
'''
nums = list((input()))

for i in range(len(nums)) :
        nums[i] = int(nums[i])

result = sum(nums)
print(result)
'''

'''
# 2-14 

입력 받은 문자열 리스트를 가나다 순으로 따로 묶으려고 합니다.
다음과 같은 리스트가 주어졌을 때 결과처럼 가나다순(사전순)으로
따로 묶은 리스트가 출력되도록 리스트 내포를 이용한 프로그램을 작성하십시오.
'''
 
'''
dicBase = (('가','깋'), ('나','닣'), ('다','딯'), ('라','맇'), ('마','밓'), ('바','빟'), ('사','싷'),

               ('아','잏'), ('자','짛'), ('차','칳'), ('카','킿'), ('타','팋'), ('파','핗'), ('하','힣'))
  

inputWord = ['막', '부모님', '비용', '비행기', '원래', '처리', '최초', '꼴', '좀', '들다', '싶다',

                   '수출', '계시다', '다', '뒤', '듣다', '함께', '아이', '무척', '보이다', '가지다', '그',

                   '자르다', '데리다', '마리', '개', '정도', '옳다', '놀이','뜨겁다']


outputWord = []
inner_unsorted = []
bundle_list = []
for bundle in dicBase : 
        for i in range(ord(bundle[0]), ord(bundle[1])+1) :
        
                bundle_list.append(chr(i))
        for j in range(len(inputWord)) :
                if inputWord[j][0] in bundle_list:
                        inner_unsorted.append(inputWord[j])
        outputWord.append(inner_unsorted)
        inner_unsorted = [] 
        
        bundle_list = []
print(outputWord)
'''
# 2-16 콤마(,)로 구분된 정수 값을 입력받아 리스트와 튜플 객체를 생성하는 코드를 작성하십시오.\

'''
nums = input().split(', ')

print(nums)

nums_list = []
for i in range(len(nums)) : 
        nums[i] = int(nums[i])

print(nums)
print(tuple(nums))
'''
# 2-17 다음의 결과와 같이 사용자로부터 콤마(,)로 구분해 여러 원의 반지름을 입력 받아 이들에 대한 원의 둘레를 계산해 출력하는 프로그램을 작성하십시오.
'''
from math import pi

def calc_circumference():
        nums = input().split(', ')
        circumference_list = []
        nums_list = []
        for i in range(len(nums)) : 
                nums[i] = float(nums[i])
                circumference = round(nums[i] * 2.00  * pi, 2)
              
                circumference_list.append(circumference)

   
        circumference_list = str(circumference_list)
        circumference_list = circumference_list.replace('[','')
        circumference_list = circumference_list.replace(']','')
        
        return circumference_list

result = calc_circumference()

print(result)
'''
# 2-18 다음과 같이 2차원 배열 구조를 만들기 위한 행, 열 정보를 콤마(,)로 구분해 입력하고, 
# 이 리스트 객체의 항목의 값은 행과 열의 인덱스 곱으로 초기화해 출력하는 프로그램을 작성하십시오.
'''
nums = input().split(', ')
row = int(nums[0])
col = int(nums[1])

list_out = []
list_in = []
for i in range(row):
        for j in range(col):
                list_in.append(i * j)
        list_out.append(list_in)
        list_in = []
print(list_out)
'''
# 2-19단어를 콤마(,)로 구분해 입력하면 그 단어들을 사전순으로 정렬해 출력하는 프로그램을 작성하시시오.
'''
words = input().split(', ')
words.sort()

print(', '.join(words))
'''

#2- 20콤마(,)로 구분해 숫자를 입력하고, 입력된 숫자 중 홀수를 콤마(,)로 구분해 출력하는 리스트 내포 기능을 이용한 프로그램을 작성하십시오.
'''
nums = input().split(', ')

for i in range(len(nums)):
        nums[i] = int(nums[i])
nums_odd = [i for i in nums if i % 2 == 1]
print(', '.join(map(str, nums_odd)))
'''

# 2-21 주어진 튜플 (1,2,3,4,5,6,7,8,9,10)의 앞 항목 절반과 뒤 항목 절반을 출력하는 프로그램을 작성하십시오.

nums = (1,2,3,4,5,6,7,8,9,10)
nums = list(nums)

a = int(len(nums)/2)

nums1 = nums[0:a]
nums2 = nums[a:]

print(tuple(nums1))
print(tuple(nums2))

