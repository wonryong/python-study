# and 연산자
# 결과값은 True와 False 둘 중 하나
# a and b : a와 b가 모두 참(True)이면 True, 둘 중 하나라도 틀리면 False

# or 연산자
# a or b : a와 b중 하나라도 참(True)이면 True가 된다. 둘 다 틀리면 False이다.

# not 연산자(!) 0이 False이다. 다른 숫자들은 모두 참(True)이다.
# True면 flase, flase면 True가 된다.

a = 10
b = 0

print(f'{a} > 0 and {b} > 0 : {a > 0 and b > 0}')
print(f'{a} > 0 or {b} > 0 : {a > 0 or b > 0}')
print(f'not {a} : {a, not a}')
print(f' not {b} : {b, not b}')