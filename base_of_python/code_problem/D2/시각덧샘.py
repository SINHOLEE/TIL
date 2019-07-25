T = int(input())

for t in range(1, T + 1):
    N = list(map(int, input().split()))


    si = N[0] + N[2]

    bun = N[1] + N[3]

    if bun >= 60:
        si += 1
        bun = bun - 60

    if si > 12:
        si = si - 12


    print(f'#{t} {si} {bun}')