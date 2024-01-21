# 정수 int

# int()함수를 이용하면 다른 자료형의 값을 정수형 데이터로 변환할 수 있다.
print(int(1.9))  # 1 / 1.9의 소수점 (.9) 이하를 제거하여 정수 1로 변환
print(int(True))  # 1 / True는 1로 변환 , 대표적 사실상 0 이외의 숫자가 들어와도 True이다.
print(int(False))  # 0 / False는 0으로 변환
print(int('100'))  # 100 / 문자열 '100'을 정수 100으로 변환
print(type(100))  # <class 'int'> : int(정수) 형이다.

# 10진수를 2진수, 8진수, 16진수로 변환하는 방법
print()
n = 95
print(type(n))  # <class 'int'>
print(bin(n))   # 0b1011111 / 2진수로 변환
print(oct(n))   # 0o137 / 8진수로 변환
print(hex(n))   # 0x5f / 16진수로 변환
