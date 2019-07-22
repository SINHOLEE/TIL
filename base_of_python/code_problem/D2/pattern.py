# T = int(input())
# words = []
# for i in range(T):
#     word = input()
#     words.append(word)

# print(words)

words = ['KOREAKOREAKOREAKOREAKOREAKOREA', 'SAMSUNGSAMSUNGSAMSUNGSAMSUNGSA', 'GALAXYGALAXYGALAXYGALAXYGALAXY']

# for char in words[0]:
#     print(char)

# word = list('KOREAKOREAKOREAKOREAKOREAKOREA')
# print(word)
# # print(word)
n = 0
for word in words:
    pattern = []
    for i in range(1, len(word)):
        if len(pattern) >= 2 and len(pattern) <= 10:
            break 
        if word[0] == word[i]:
            pattern.append(word[0])
            for j in range(i - 1):
                if word[j + 1] == word[i + j + 1]:
                    pattern.append(word[j + 1])
                else:
                    pattern = []
                    pass
    n += 1
    print(f'#{n} {len(pattern)}')


