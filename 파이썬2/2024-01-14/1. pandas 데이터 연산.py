import pandas as pd
import numpy as np

s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([10, 20, 30, 40, 50])
print(s1 + s2)
# 다른 사칙연산도 가능

# * : 중요
# 파이썬의 리스트와 numpy의 배열은 서로 크기가 다르면 연산이 불가능
# 하지만 pandas의 데이터 끼리는 서로 크기가 달라도 가능
# 이 경우 연산을 할 수 있는 항목만 연산을 수행
s11 = np.array([1, 2, 3, 4])
s22 = np.array([1, 2, 3, 4, 5])
s3 = pd.Series([1, 2, 3, 4])
s4 = pd.Series([10, 20, 30, 40, 50])
# print(s11 + s22)
print(s3 + s4)

data = {'Date': ['2024-01-14', '2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19'],
        'Company': ['삼성', '테슬라', '애플', 'LG', '기아', '현대'],
        'price': [145.12, 146.34, 2567.89, 2556.78, 277.65, 280.12]}

df = pd.DataFrame(data)

# groupby : 특정 기준에 따라 그룹으로 나누는데 사용

# 각 회사별로 최고 주가를 기록한 날짜와 해당 주가 출력
max_price = df.groupby('Company')['price'].max()
max_date = df.groupby(['Company', 'price'])['Date'].first()

result = pd.concat([max_date, max_price], axis=0)
result.columns = ['Date', 'max_price']

# print(max_price)

print(result)

# df는 데이터 프레임 , key는 그룹화에 사용할 열(열의 리스트)

# concat : 여러개의 데이터 프레임을 연결하여 하나의 데이터 프레임으로 합치는데 사용
# 유의점 : concat은 인덱스를 유지한 상태로 데이터 프레임을 연결
# 중복되는 열(또는 인덱스)가 있는 경우 : 연결된 결과는 중복된 열이 포함된다.
# concat은 원본 데이터 프레임을 변경하지 않고 새로운 데이터 프레임을 생성한다.


