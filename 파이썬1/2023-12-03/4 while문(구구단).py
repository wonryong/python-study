# 구구단 2단 부터 9단까지 출력
# 각 단 앞에 제목, 마지막에 구분선을 넣어 볼 것

dan = 2

while dan <= 9:
    n = 1
    while n <= 9:
        print(f'{dan} x {n} = {dan * n}')
        n += 1
    print(f'{dan}단이 끝났습니다.')
    dan += 1