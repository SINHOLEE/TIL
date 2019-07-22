
def repeat_sqrt(x, b = 1, v   ):
    v = x
    if abs(x ** 2 - b ** 2) <= 1e-10:
        return f'{a:0.3f}'
    elif v < ((x + b) / 2) ** 2:
        return repeat_sqrt(((x + b) / 2), b, v = 1)
    else:
        return repeat_sqrt( x, ((x + b) / 2), v = 1)


b = repeat_sqrt(10 )
print(b)

#양의 정수 x를 받으면서 기존의 양의 정수 x와 비교하는 재귀를 쓰려면 부득이하게 변수를 두 개 받았습니다.