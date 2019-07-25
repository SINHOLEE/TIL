import sys
sys.stdin = open('GNS_test_input.txt', 'r')
sys.stdout = open('GNS_test_input_w.txt', 'w', encoding='utf-8')


T = int(input())
aa = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
b = dict(enumerate(aa))
# print(b)
for t in range(1, T + 1):
    a, tc_nums = input().split()
    tc_nums = int(tc_nums)
    temp = list(map(str, input().split()))
    print(f'\n{a}')
    new = []
    # 단어개수 counting

    for key, value in b.items():
        c  = temp.count(value)
        new.append(c)
    my_list = {key : value for key, value in zip(aa,new) }

    for key, value in my_list.items():
        print(f'{key} ' * value, end=' ')

