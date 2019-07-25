T = int(input())

for t in range(1,T + 1):
    N = int(input())
    for i in range(1, N + 1):
        result = 0
        if i % 2 == 1:
            i = i
        else:
            i = -1 * i

        result += i
    print(f'#{t} {result}')