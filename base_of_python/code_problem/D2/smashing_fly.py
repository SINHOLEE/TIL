T = int(input())

for i in range(1, T + 1):
    N, M = map(int, input().split()) # N은 매트릭스 크기, M은 파리채 크기
    matrix = []
    for row in range(1, N + 1):
        temp_dict = {
            f'row{row}' : list(map(int, input().split()))
            }
        matrix.append(temp_dict)
        print(matrix)