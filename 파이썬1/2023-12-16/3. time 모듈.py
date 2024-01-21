# 3. time 모듈
import time

# 1) time() 함수
# 1970년 1월 1일 0시 0분 0초 부터 현재까지 경과된 시간 timestamp 반환
# 소수점 이하는 마이크로 초를 의미
print(time.time())  # 1702711345.6705008

# 2) ctime() 함수
# 인수로 전달된 시간 timestamp 형식에 맞춰 반환
print(time.ctime(time.time()))  # Sat Dec 16 16:23:39 2023

# 3) sleep() 함수
# 인수로 전달된 초 second 만큼 시스템을 일시 정지

time.sleep(3)

# 4. datetime 모듈
# 날짜와 시간 데이터를 처리할 때 사용
print()
import datetime

# 1) now() 메소드
# datetime 클래스 내부에 정의된 메소드
# 시스템의 현재 날짜와 시간을 반환
present = datetime.datetime.now()
print(present)  # 2023-12-16 16:26:17.837524

# 2) date() 함수
# 특정 날짜를 반환
birthday = datetime.datetime(2023, 12, 16)
print(birthday)
