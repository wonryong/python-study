import pandas as pd

# 인덱스 범위 지정만이 목적
# 시작 날짜와 끝 날짜를 지정해 데이터를 생성. 하루씩 증가한 날짜 데이터가 생성된다.
# print(pd.date_range(start='2024-01-13', end='2024-01-31'))

# 날짜 데이터를 입력할 때 yyyy-mm-dd 형식이 아니라
# yyyy/mm/dd, yyyy.mm.dd, mm-dd,yyyy, mm/dd/yyyy, mm.dd.yyyy 같은 형식도 사용 가능
# 대신 출력은 yyyy-mm-dd 형식으로 실행
print(pd.date_range(start='2024/01/01', end='2024.1.13'))

# 끝 날짜를 지정하지 않고 periods 만 입력해서 날짜 생성
print(pd.date_range(start='01-01-2024', periods=7))  # 얼마만큼 날짜를 추가하겠다.

# 약어     설명    사용 예
#  D      달력    날짜 기준 하루 주기 ex) 하루주기 : freq = 'D' 이틀추기 : freq = '2D'
#  B      업무    날짜  기준 하루 주기 ex) 업무일(월~금) 기준으로 생성,

# 2일씩 증가하는 날짜를 생성

print(pd.date_range(start='2024-01-01', periods=4, freq='2D'))

# 달력의 요일을 기준으로 일주일씩 증가하는 날짜를 생성
print(pd.date_range(start='2024-01-01', periods=12, freq='B'))

# 분기 시작일을 기준으로 4개의 날짜를 생성
print(pd.date_range(start='2024-01-01', periods=4, freq='QS'))

# 연도의 첫날을 기준으로 1년 주기의 3개의 날짜 생성

print(pd.date_range(start='2024-01-01', periods=3, freq='AS'))

# 날짜뿐 아니라 시간을 생성

# 1시간 주기로 10개의 시간을 생성

print(pd.date_range(start='2024-01-01 08:00', periods=10, freq='H'))

# 30분 단위로 4개의 시간을 생성

# 30min으로 설정해도 출력은 30T
print(pd.date_range(start='2024-01-01 08:00', periods=4, freq='30min'))

# S = 초, 10S = 10초마다 출력
print(pd.date_range(start='2024-01-01 10:00',periods=5,freq='10S'))

# 문제 : date_range() 함수를 사용하여 2024년 1월 1일부터 2024년 12월 31일까지의 인덱스를 갖는 데이터 프레임을 생성하시오.

data = pd.date_range(start='2024-01-01',end='2024-12-31')

print(data)