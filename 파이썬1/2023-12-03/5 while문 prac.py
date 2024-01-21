# 정수를 입력받아서 그 횟수만큼 'Hello'를 출력하는 프로그램을 구현하세요.
# 0 이하의 값이 입력되면 '잘못된 입력입니다.' 라는 오류 메시지를 출력하세요.

# 실행 예)
# 정수를 입력하세요 >>> 5
# 1번째 Hello
# 2번째 Hello
# 3번째 Hello
# 4번째 Hello
# 5번째 Hello

# 정수를 입력하세요 >>> -5
# 잘못된 입력입니다.

# n = int(input('정수를 입력하세요 >>> '))
# b = 1
# if n <= 0:
#     print('잘못된 입력입니다.')
#     exit()
# while b <= n:
#     print(f'{b}번째 hello')
#     b += 1

count = int(input('정수를 입력하세요 >>> '))
if count <= 0:
    print('잘못된 입력입니다.')
else:
    n = 1
    while n <= count:
        print(f'{n}번째 hello')
        n += 1