T = int(input())

for testcase in range(1, T + 1):
    N = int(input())
    p_triangle = []
    a = []
    for n in range(1, N + 1):
        if n == 1:
            a.append(n)
            p_triangle.append({f'a_{n}' : a})
            # print(f' n = {n}, p_triangle = {p_triangle} ')
            a = []
        elif n == 2:
            a =[1, 1]
            p_triangle.append({f'a_{n}' : a})
            # print(f' n = {n}, p_triangle = {p_triangle} ')
            a = []
            
        else:
            for i in range(len(p_triangle[-1].get(f'a_{n - 1}')) - 1):  # p_triangle[-1].get(f'a_{n - 1}') -> a_(n-1)의 value -> 이전 항의 리스트
                # print(i)
                
                a.append(sum(p_triangle[-1].get(f'a_{n - 1}')[0 + i:2 + i])) 
            a.insert(0, 1)
            a.append(1)
            # for i in range(len(p_triangle[n - 2].get(f'a_{n - 1}') - 1))
            # a.append(sum(p_triangle[n - 1].get(f'a_{n - 1}')))
            p_triangle.append({f'a_{n}' : a})
            a = []
    print(f'#{n}')
    for dict_a in p_triangle:
        for key, value in dict_a.items():
            print(' '.join(map(str, value)))


            # print(' '.join(map(int, temp)))
        # print()
        # print(str(x) for x in list(dict_a.values())[0])
        # # print(' '.join(map(int, str(list(dict_a.values())[0]))))

        # # print(p_triangle)