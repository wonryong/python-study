# pandas 라이브러리 : 파이썬에서 데이터 분석과 처리를 쉽게 처리할 수 있게 도와준다.
# pandas : 어디에 쓰이냐? AI,머신러닝(인공지능), 딥러닝, 그래프를 뽑아내기 위해

# pandas는 numpy를 기반으로 만들어졌지만 좀 더 복잡한 데이터 분석에 특화
# numpy가 같은 데이터 타입의 배열만 처리할 수 있는데 반해 pandas는 데이터 타입이 다양하게 섞여 있어도 처리가 가능

# 공식 홈페이지 : https://pandas.pydata.org/

# 1. 구조적 데이터 생성하기

# 1) Series를 활용한 데이터 생성
import pandas as pd

# pandas에서 데이터를 생성하는 가장 기본적인 방법은 Series()를 이용하는 것.
# Series()를 이용하면 Series 형식의 구조적 데이터(라벨을 갖는 1차원적 데이터)를 생성할 수 있다.
# 다음은 Series()를 이용해 Series 형식의 데이터를 생성하는 방법.
# s = pd.Series(seq_data)
# Series() 인자로는 시퀀스 데이터가 들어간다.
# 시퀀스 데이터 : 리스트와 튜플 타입의 데이터(모두 사용할 수 있다) 주로 리스트 데이터를 많이 사용

s1 = pd.Series([10, 20, 30, 40, 50])
print(s1)

# 자동으로 데이터 라벨(0~4) 부여되고, 세로출 라벨을 index라고 하고, 시퀀스 데이터는 values라고 한다.

# Series 데이터는 index와 value를 분리해서 가져 올 수 있다.
# Series 데이터를 s라고 할 때 index는 s.index로, values는 s.values로 가져 올 수 있다.
print(s1.index)

print(s1.values)

# numpy의 경우 배열의 모든 원소가 데이터 타입이 같아야 하지만,
# pandas의 경우 원소의 데이터 타입이 달라도 가능

s2 = pd.Series(['a', 'b', 'c', 1, 2, 3])
print(s2)

# dtype: object
# 변수 s2는 문자열과 숫자가 혼합이 되어 있어 타입이 object = 모든것

# 데이터가 없는경우. numpy를 임포트 한 후 np.nan으로 데이터가 없음을 표시 할 수 있다.
import numpy as np

s3 = pd.Series([np.nan, 10, 30])
print(s3)
# 데이터를 위한자리 index는 있지만 실제 값은 없다.

# Series 데이터를 생성할 때 다음과 같이 인자로 index 추가 가능.
# s = pd.Series(seq.data, index = index_seq)
# 인자로 index를 명시적으로 입력하면 Series 변수 (s)의 index는 자동생성되는 index대신 index_seq가 들어가게 된다.
# index_seq도 리스트와 튜플 타입의 데이터를 모두 사용하지만 주로 리스트를 사용한다.
# 주의할점은 seq_data의 항목 개수와 index_seq의 항목 개수가 같아야 한다.

# 어느 가게의 날짜별 판매량을 pandas의 Series 형식으로 입력. 하루는 데이터가 없어서 np.nan으로 입력

index_data = ['2024-01-13', '2024-01-14', '2024-01-15', '2024-01-16']
s4 = pd.Series([200, 195, np.nan, 205], index=index_data)
print(s4)

# 파이썬의 딕셔너리를 사용하면 데이터와 index를 함께 입력할 수 있다.
# s = pd.Series(dict_data)
# 입력 인자로 딕셔너리 데이터를 입력하면 딕셔너리 데이터의 키(key) 와 값(value)가 각각
# Series 데이터의 index와 values로 들어가게 된다.

s5 = pd.Series({'국어': 100, '영어': 80, '수학': 90})
print(s5)

# DataFrame 은 2차원 형태의 표 형식 데이터 구조로 행과 열로 구성된다.
# 각 열은 데이터의 특성을 나타내며, 각 행은 데이터의 인스턴스를 나타낸다. 각 셀은 단일 데이터 값을 가질 수 있다.
# 어디에 쓰이냐? : 데이터 과학, 통계 분석, 비즈니스 분석

# DataFrame()으로 생성한 데이터의 예
table_data1 = {'A': [1, 2, 3, 4, 5],
               'B': [10, 20, 30, 40, 50],
               'C': [100, 200, 300, 400, 500]}
df1 = pd.DataFrame(table_data1)
print(df1)

table_data2 = {'A': [6, 7, 8],
               'B': [60, 70, 80],
               'C': [600, 700, 800]}
df2 = pd.DataFrame(table_data2)
print(df2)

# 두 개의 DataFrame 데이터 df1과 df2는 길이가 같지 않음
# 길이가 같지 않더라도 연산이 가능
print(df1 + df2)

# Series와 마찬가지로 DataFrame도 연산할 수 있는 항목 끼리만 연산하고, 그렇지 못한 항목은 NaN으로 표시

# pandas에는 데이터의 통계 분석을 위한 메서드(함수:호출) 이 있어서 데이터의 총합, 평균, 표준 편차 등을 쉽게 구할 수 있다.
# 2012년 부터 2016년 까지 우리나라의 계절별 강수량(단위 mm)

table_data3 = {'봄': [256.5, 264.3, 215.9, 223.2, 312.8],
               '여름': [770.6, 567.5, 599.8, 387.1, 446.2],
               '가을': [363.5, 231.2, 293.1, 247.7, 381.6],
               '겨울': [139.3, 59.9, 76.9, 109.1, 108.1]}

columns_list = ['봄', '여름', '가을', '겨울']
index_list = ['2012', '2013', '2014', '2015', '2016']

df3 = pd.DataFrame(table_data3, columns=columns_list, index=index_list)
print(df3)

# pandas에서 제공하는 통계 메서드는 원소의 합을 구하는 sum(), 평균 : mean(), 표준 편차 : std(), 분산 : var(), 최솟값 : min(), 최댓값 : max(), 각 원소에 누적 합을 구하는 cumsum(), 누적 곱 : cumprod()

print(df3.mean())

print(df3.std())

# 연도별로 평균 강수량과 표준 편차를 구할 경우엔 연산의 방향 설정을 위해 axis 인자를 추가
# axis가 0이면 DataFrame의 values에서 열별로 연산을 수행, 1이면 행별로 연산을 수행
print(df3.mean(axis=1))

# describe()를 이용하면 평균, 표준편차, 최솟값과 최댓값 등을 한 번에 구할 수 있다.
# 25% / 50% / 75% : 백분위수의 각 지점으로, 분포를 반영해 평균을 보완하는 목적으로도 사용 가능
print(df3.describe())

import pandas as pd

data = {'Name': ['John', 'Mike', 'Sarah', 'Kate'],
        'Age': [32, 28, 45, 36],
        'City': ['Seoul', 'New York', 'Paris', 'London']}

# 판다스를 사용해 데이터 프레임에서 Age열의 평균을 구하시오.
# hint : 데이터 프레임은 리스트, 튜플 형식이라 생각하면 편하다.

df = pd.DataFrame(data)
print(df)
age = df['Age'].mean()
print(age)
