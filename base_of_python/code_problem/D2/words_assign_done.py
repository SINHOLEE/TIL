import sys
sys.stdin = open('input_words_assign.txt', 'r')
sys.stdout = open('input_words_assign_w.txt', 'w', encoding='utf-8')
try:
    T = int(input())
    list_nk = []
    matrix = []
    matrix_list = []
    for i in range(T):

        # 각 케이스의 n과 k값을 받는 부분
        nk = list(map(int,input().split()))
        list_nk.append(nk)
        # print(list_nk)
        if nk[0] < 5 or nk[0] > 15 :
            raise ValueError
            pass
        if nk[1] < 2 or nk[1] > nk[0] :
            raise IndexError
            pass

        for j in range(nk[0]):

        # 각 케이스의 단어퍼즐 받는 부분
            temp = list(map(int,input().split()))
            matrix.append(temp)
            
        matrix_list.append(matrix)
        matrix = []
        # print(matrix_list) matrix_list[z][i][j] z = #n, i = 행번호, j = 열번

    # list_nk[0][0], list_nk[1][0], list_nk[2][0] = n
    # list_nk[0][1], list_nk[0][1], list_nk[0][1] = k
    '''
    [
    [[1, 1, 0, 0, 1], 
    [1, 1, 1, 0, 1], 
    [1, 1, 1, 0, 0], 
    [1, 1, 1, 0, 1], 
    [1, 1, 1, 0, 0]], 

    [[1, 1, 1, 0, 1], 
    [1, 0, 1, 0, 1], 
    [1, 0, 1, 0, 1], 
    [1, 1, 1, 0, 1], 
    [1, 1, 1, 0, 0]]
    ]
        '''

                
                
                    


    count = 0
    matrix_r =[]
    mat_temp = []





    for z in range(len(matrix_list)):
        matrix_r = []
        mat_temp = []
        count = 0
        for i in range(len(matrix_list[z])):
            for j in range(len(matrix_list[z][i])):
                mat_temp.append(matrix_list[z][j][i])
            matrix_r.append(mat_temp)
            mat_temp = []
        

        
        for i in range(len(matrix_list[z])):   
            temp = 0
                
            for j in range(len(matrix_list[z][i])):
                if matrix_list[z][i][j] == 1:
                    if temp == list_nk[z][1]: # 0 은 z로 받기

                        count -= 1
                        temp = 0
                        # print(f'z={z}, i={i},j={j},n={n}temp bi= {list_nk[z][1]}, item =  {matrix_list[z][i]}, j = {matrix_list[z][i][j]}, temp = {temp}, count = {count}')
                            
                    else:
                        temp += 1
                        # print(f'z={z}, i={i},j={j},n={n}temp bi= {list_nk[z][1]}, item =  {matrix_list[z][i]}, j = {matrix_list[z][i][j]}, temp = {temp}, count = {count}')
                        if temp == list_nk[z][1]: # 0 은 z로 받기
                            count += 1
                            # print(f'z={z}, i={i},j={j},n={n}temp bi= {list_nk[z][1]}, item =  {matrix_list[z][i]}, j = {matrix_list[z][i][j]}, temp = {temp}, count = {count}')
                
                else:   
                    temp = 0
                    # print(f'z={z}, i={i},j={j},n={n}temp bi= {list_nk[z][1]}, item =  {matrix_list[z][i]}, j = {matrix_list[z][i][j]}, temp = {temp}, count = {count}')
    
        for i in matrix_r: 
            
            temp = 0
        
            for j in i:
                if j == 1:
                    if temp == list_nk[z][1]: # 0 은 z로 받기
                        count -= 1
                        temp = 0
                        # print(f'z={z}, i={i},j={j},n={n}temp bi= {list_nk[z][1]}, item =  {matrix_r[i]}, j = {j}, temp = {temp}, count = {count}')
                            
                    else:
                        temp += 1
                        # print(f'z={z}, i={i},j={j},n={n}temp bi= {list_nk[z][1]}, item =  {matrix_r[i]}, j = {j}, temp = {temp}, count = {count}')
                        if temp == list_nk[z][1]: # 0 은 z로 받기
                            count += 1
                            # print(f'z={z}, i={i},j={j},n={n}temp bi= {list_nk[z][1]}, item =  {matrix_r[i]}, j = {j}, temp = {temp}, count = {count}')
                else:   
                    temp = 0
                    # print(f'z={z}, i={i},j={j},n={n}temp bi= {list_nk[z][1]}, item =  {matrix_r[i]}, j = {j}, temp = {temp}, count = {count}')
    
        print(f'#{z+1} {count}')
except ValueError:
    print('n이 5 이상 15 이하의 정수가 아닙니다.')
except IndexError:
    print('k가 2 이상 n이하의 정수가 아닙니다.')
