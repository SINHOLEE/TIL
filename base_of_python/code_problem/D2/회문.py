T = int(input())

for t in range(1, T + 1):
    word = input()
    if word[:] == word[::-1]:
        result = 1
    else:
        result = 0
        
    print(f'#{t} {result}')
