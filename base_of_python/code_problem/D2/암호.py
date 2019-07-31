T = int(input())
for t in range(1, T + 1):
    N = int(input())
    word = ''
    for n in range(1 , N + 1):
        C, K = input().split()
        K = int(K)
        word += C * K
    print('#', end='')
    print(t)
    while len(word[0:10]) >= 10:
        print(word[0:10])
        word = word[10:]
    print(word)