'''

2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.


[제약 사항]

각 수는 0 이상 10000 이하의 정수이다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 2개의 수가 주어진다.


[출력]

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

 (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''
try:
    first = int(input())
    list_input = []

    for i in range(first):
        temp = list(map(int, input().split()))
        if len(temp) == 2:
            # print('len(temp)',len(temp))
            # print('temp의 len이 2라면 출력')  #디버그 테스트 용
            pass
        else:
            # print('len(temp) 가 2가 아니라면 출력')  #디버그 테스트 용
            raise Exception       
        list_input.append(temp)
        

    for i in range(len(list_input)):
        for j in range(len(list_input[i])):
            if list_input[i][j] >= 0 and list_input[i][j] <= 10000 :
                # print('두수를 받을 때 조건에 충족하다면')  #디버그 테스트 용
                pass
            else:
                # print('0에서 10000사이의 숫자를 받지 않았다면')  #디버그 테스트 용
                raise ValueError
    
    for i in range(len(list_input)):
        if list_input[i][0] < list_input[i][1]:
            result = '<'
        elif list_input[i][0] == list_input[i][1]:
            result = '='
        else:
            result = '>'
        
        print(f'#{i+1} {result}')

except ValueError:
    print('0 에서 10000사이의 정수를 입력해주십시오.')

except Exception:
    print('두 정수를 입력하십시오.')

