T = int(input())
for t in range(1, T + 1):
    n = int(input())
    list_num = [2,3,5,7,11]
    zzz = []
    for i in list_num:
        count = 0
        while n % i == 0:
            n  = int(n / i)
            count += 1
        zzz.append(count)
    print(f'#{t} {zzz[0]} {zzz[1]} {zzz[2]} {zzz[3]} {zzz[4]}')

