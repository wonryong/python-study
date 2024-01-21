import pandas as pd
import numpy as np
# 1. 주어진 데이터 프레임 df에는 Name "이름", Age (나이), Salary(월급) 열이 있다.
# 주어진 데이터 프레임은 다음과 같다.

#    Name  Age  Salary
# 0   Amy   25   3000
# 1   Bob   30   4000
# 2  Chad   35   5000
# 3  Dave   40   6000
# 4  Emma   45   7000


data = {
    'Name': ['Amy', 'Bob', 'Chad', 'Dave', 'Emma'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [3000, 4000, 5000, 6000, 7000]
}

df = pd.DataFrame(data)

# 1. Salary열의 평균값을 계산하시오.
average_salary = df['Salary'].mean()
print("Salary 열의 평균값:", average_salary)

# 2. Age열의 최댓값을 계산하시오.
max_age = df['Age'].max()
print("Age 열의 최댓값:", max_age)

# 3. Name열에서 a를 포함한 이름만 선택하여 출력하시오.
# hint : .contains() 함수를 알아보고 만드시오.
names_with_a = df[df['Name'].str.contains('a')]
# name2 = df['Name'].str.contains('a')

# .str : 문자열 데이터를 처리하기 위한 문자열 메서드를 제공해준다.

# print(name2)
# print("Name 열에서 'a'를 포함한 이름:")
print(names_with_a['Name'])

