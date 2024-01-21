# 1부터 10사이의 모든 정수를 역순으로 출력

n = 10
while n >= 1:
    print(n)
    n -= 1 # n = n - 1

# 100부터 50 사이의 짝수를 출력
n = 100
while n >= 50:
    print(n)
    n -= 2 # n = n -2

n = 100
while n >= 50:
    if (n % 2 == 0):
        print(n)
    n -= 1