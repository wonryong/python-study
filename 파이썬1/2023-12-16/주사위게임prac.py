# 다음은 컴퓨터가 주사위를 던지면 사용자가 주사위의 숫자를 맞추는 프로그램입니다.
# 사용자가 맞힐 때까지 게임은 계속됩니다

import random

dice = random.randint(1, 6)  # 1 ~ 6 사이의 임의의 정수 하나를 반환
print(dice)
while True:
    user = int(input('주사위 값은 얼마일까요? >>> '))
    if dice == user:
        print(f'{dice}! 정답입니다.')
        break

    else:
        print('오답입니다. 다시 시도하세요.')
        if dice < user:
            print('다운')
        else:
            print('업')