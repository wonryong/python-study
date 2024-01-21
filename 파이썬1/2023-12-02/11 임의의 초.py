# 1분은 60초이고, 1시간은 60분입니다. 따라서 1시간은 3600초입니다.
# 임의의 초를 입력받아 해당 초를 시, 분,초로 변환하여 출력하는 프로그램을 구현하세요.

times = int(input('초를 입력하세요 >>> '))

hour = times // 3600
minute = times % 3600 // 60
second = times % 60
print(f'변환 결과는 {hour}시간 {minute}분 {second} 초입니다 ')