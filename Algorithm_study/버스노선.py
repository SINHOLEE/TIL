T = int(input())

for tc in range(1, T+1):
    N = int(input())
    bus_route = []  # bus [[1, 2, 3], [2, 3, 4, 5]]
    for n in range(N):
        temp = list(map(int,input().split()))
        temp = list(range(temp[0], temp[1]+1))
        bus_route += [temp]
    P = int(input())
    bus_stop = []
    result = [0] * P
    for p in range(P):
        num = int(input())
        bus_stop += [num]

    for br in bus_route:
        for bs_num in range(len(bus_stop)):
            if bus_stop[bs_num] in br:
                result[bs_num] += 1

    final = ' '.join(map(str,result))
    print('#{} {}'.format(tc, final))