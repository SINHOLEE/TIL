
def snail_cover(n):
    original_n = n
    nums = list(range(1, n ** 2 + 1))
    # print(nums)
    matrix_zero = []
    temp = []
    for i in range(n):
        for j in range(n):
            temp.append(0)
        matrix_zero.append(temp)
        temp = []
    # matrix_zero[0][0] = 1

    # print(matrix_zero)
    # print('-'*40)

    row_index = 0
    col_index = 0
    temp = []
    
    i = 0
    j = 0

    if n % 2 == 1:
        x = int((n - 1) / 2)
       
        matrix_zero[x][x] = nums.pop()
     
    while n >= 1:
        if n < 1:
            pass
    
        else:
            cap = []
            for v in range(((n - 1) * 4)):
                cap.append(nums.pop(0))

                    
            move_rt = cap[0:n-1]
            move_dw = cap[n-1:(n - 1) * 2]
            move_lf = cap[(n - 1) * 2:(n - 1) * 3]
            move_up = cap[(n - 1) * 3:]
                    
            
            # start_point_for_move_rt 0, 0 
            # start_point_for_move_dw 0, n-1
            # start_point_for_move_lf n-1, n-1
            # start_point_for_move_up n-1, 0
            
            for z in range(len(move_rt)):
                matrix_zero[0+i][z+j] = move_rt[z]
            for z in range(len(move_dw)):
                matrix_zero[z+i][n-1+j] = move_dw[z]
            for z in range(len(move_lf)):
                matrix_zero[n-1+i][n-1-z+j] = move_lf[z]
            for z in range(len(move_up)):
                matrix_zero[n-1-z+i][0+j] = move_up[z]
                
        n -= 2
        i += 1
        j += 1
    print(f'#{original_n}')
    for row in matrix_zero:
        t = ' '.join(map(str, row))
        print(t)




# aa = [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]

try:
    T = int(input())
        
    
    for r in range(T):
        N = int(input())
        if N < 1 or N > 10:
            raise ValueError
        snail_cover(N)

except ValueError:
    print('N이 1이상 10이하의 정수가 아닙니다.')