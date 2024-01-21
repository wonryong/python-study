import pandas as pd

data = {'Name': ['John', 'Mike', 'Sarah', 'Kate'],
        'Math': [90, 80, 95, 75],
        'English': [85, 90, 92, 88],
        'Science': [92, 88, 78, 80]}

df = pd.DataFrame(data)

# 각 학생의 총점을 계산하고 싶다.

df['Total'] = df['Math'] + df['English'] + df['Science']

print(df)

# 3) DataFrame을 활용한 데이터 생성
# 표 Table과 2차원 데이터 처리를 위해 DataFrame을 제공.
# 데이터 Data를 담는 틀 Frame이라는 뜻

# DataFrame을 이용해 데이터를 생성하는 방법
# df = pd.DataFrame(data, [, index = index_data, columns = columns_data])
# data 인자에는 리스트와 형태가 유사한 데이터 타입은 모두 사용 가능.
# 즉 리스트, 딕셔너리 numpy의 배열 데이터, Series나 DataFrame 타입의 데이터는 입력이 가능하다.
# 세로축 라벨을 index라 하고, 가로축 라벨을 columns라고 한다.
# index와 columns를 제외한 부분으로 values라고 한다.

import pandas as pd

d1 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(d1)
# values 부분에는 일정한 data가 순서대로 입력되어 있고
# 가장 좌측을 열과 가장 윗줄의 행에는 각각 숫자가 자동으로 생성되어 index, columns를 구성

# 명시적으로 index와 columns를 입력하지 않더라도 자동으로 index, columns가 생성되는 구조이다.

# numpy 배열 데이터를 입력해 생성한 DataFrame 데이터의 예
import numpy as np

data_list = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
d2 = pd.DataFrame(data_list)
print(d2)

# data뿐만 아니라 index와 columns도 지정한 예
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
index_date = pd.date_range('2024-01-01', periods=4)
columns_list = ['A', 'B', 'C']
d3 = pd.DataFrame(data, index=index_date, columns=columns_list)
print(d3)

# 딕셔너리 타입으로 2차원 데이터를 입력한 예
table_data = {'연도': [2015, 2016, 2016, 2017, 2017],
              '지사': ['한국', '한국', '미국', '한국', '일본'],
              '고객수': [200, 250, 450, 300, 500]}
d4 = pd.DataFrame(table_data)
print(d4)

d5 = pd.DataFrame(table_data, columns=['지사', '고객수', '연도'])
print(d5)

# DataFrame 데이터에서 index, columns, values를 각각 구한 예
print(d5.index)
print(d5.columns)
print(d5.values)