# 1부터 100사이의 모든 정수 중에서 7의 배수만 출력하는 프로그램을 구현하세요.

a = 1
while a <= 100:
    if a % 7 == 0:
        print(a)
    a += 1

n = 7
while n <= 100:
    print(n)
    n += 7