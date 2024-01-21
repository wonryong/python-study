
# 700원자리 음료수를 뽑을 수 있는 자판기 프로그램을 구현하세요.
# 돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지 그리고 잔돈은 얼마인지 모든 경우의 수를 출력하도록 구현하세요.

# 함수 정의
# *반환값 : 없음
# 함수 이름 : vending_machine()
# 매개변수 : 정수 money

# 코드 구성
# def vending_machine(money)
#  함수 구현

# vending_machine(3000)

# 실행 예)
# 음료수 = 0개, 잔돈 = 3000원
# 음료수 = 1개, 잔돈 = 2300원
# 음료수 = 2개, 잔돈 = 1600원
# 음료수 = 3개, 잔돈 = 900원
# 음료수 = 4개, 잔돈 = 200원

def vending_machine(money):
    price = 700
    count = money // price
    for drink in range(count + 1):
        change = money - drink * price
        print(f'음료수 = {drink}개, 잔돈 = {change}')

vending_machine(3000)

