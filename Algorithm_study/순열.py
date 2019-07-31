# for문으로 1, 2, 3 의 순열 구하기.

for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i1 != i2:
            for i3 in range(1, 4):
                if i2 != i3 and i1 != i3:
                    print(i1, i2, i3)