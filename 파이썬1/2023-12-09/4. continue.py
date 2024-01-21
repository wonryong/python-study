# continue 문
# 반복문의 시작 지점으로 제어의 흐름을 옮기는 역활
# 반복에서 제외하거나 생략하고 싶은 코드가 존재할 때 사용

# 1에서 100사이의 모든 정수를 합하는데 3의 배수만 제외
total = 0
for i in range(1,101):
    if i % 3 == 0: # 3의 배수인지 확인한다.
        continue
    total += i
print(total)

# continue를 사용하지 않고 3의 배수는 제외해서 문제를 풀어보시오.
total = 0
for i in range(1,101):
    if i % 3 != 0:
        total += i
print(total)