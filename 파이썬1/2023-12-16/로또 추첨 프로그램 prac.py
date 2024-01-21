
# 로또 추첨 프로그램은 당첨번호가 총 6개가 나온다. 1 ~ 45의 숫자중에 뽑아내면 된다.




import random
import time

# 당첨번호를 저장할 리스트
jackpot = []

while len(jackpot) < 6:
    # 1부터 45 사이의 랜덤한 번호 생성
    num = random.randint(1, 45)

    # 이미 당첨번호 리스트에 있는 번호인지 확인
    if num not in jackpot:
        # 중복되지 않는 경우에만 리스트에 추가
        jackpot.append(num)
        print(f'{len(jackpot)}번째 당첨번호는 {num}입니다.')
        time.sleep(2)

# 당첨번호를 정렬하여 출력
jackpot.sort()
print(f'이번 당첨번호는 {jackpot}입니다.')
