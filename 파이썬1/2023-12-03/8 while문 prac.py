# 0 ~ 9 사이의 정수를 입력을 받습니다.
# 받을 수 있는 기회는 5번이다.
# 5번을 받고나면 '모두 입력되었습니다.' -> '입력된 값은 ~~ 입니다.
# 제약 : 0 ~ 9 사이의 정수를 받지만 같은 정수를 받을 시 하나로 입력된다.

my_list = []
a = 5

while a >= 1:
    print(f'총 기회는 {a}번 남았습니다.')
    b = int(input('0 ~ 9 사이 정수를 입력하세요 >>> '))
    my_list.append(b)
    a -= 1
print('모두 입력되었습니다.')
print(f'입력된 값은 {set(my_list)}')