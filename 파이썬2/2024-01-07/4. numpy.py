# 2. 배열의 연산
import numpy as np

# 1) 기본연산
# 배열의 형태 shape(행,열)이 같다면 덧셈과 뺄셈, 곱셈, 나눗셈 연산을 할 수 있다.

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([1, 2, 3, 4, 5])

# 각 배열의 같은 위치의 원소끼리 더함
print(arr1 + arr2)

# 각 배열의 같은 위치의 원소끼리 뺀다
print(arr1 - arr2)

# 배열에 상수를 곱하면 각 원소에 상수를 곱함.
print(arr1 * 2)

# 배열의 거듭제곱은 각 원소에 거듭제곱
print(arr1 ** 2)

# 두 배열의 나눗셈은 각 원소끼리 나눔
print(arr1 / arr2)

# 복합연산
print(arr1 / (arr2 ** 2))

# 배열은 비교 연산도 가능하다. 원소별로 조건과 일치하는지 검사한 후 일치하면 True를, 그렇지 않으면 False를 반환

print(arr1 > 20)

# 2) 통계를 위한 연산
# Numpy에는 배열의 합, 평균, 표준 편차, 분산, 최솟값과 최댓값, 누적 합, 누적곱 등 주로 통계에서 많이 이용하는 메서드가 포함되어 있다.

arr3 = np.arange(5)
print(arr3)

# 불편할 수도 있고 비효율적.
# arrsum = 0
# for i in range(5):
#     print(arr3[i])
#     arrsum += arr3[i]
#
# print(arrsum)
# print(arr3[0] + arr3[1] + arr3[2])

# 합
print(arr3.sum())

# 평균
print(arr3.mean())

# 표준 편차 : 데이터가 얼마나 평균값에서 퍼져 있는지를 나타내주는 통계
print(arr3.std())

# 분산 : 단점 : 분산은 제곱의 형태로 값을 가진다. 그래서 원래 데이터와 다른 형태로 나타나는 단점이 존재.

print(arr3.var())

# 최솟값
print(arr3.min())

# 최댓값
print(arr3.max())

arr4 = np.arange(1, 5)
print(arr4)

# 누적합
print(arr4.cumsum())

# 누적곱
print(arr4.cumprod())

# 행렬 연산
# NumPy는 배열의 단순 연산뿐 아니라 선형 다수를 위한 행렬(2차원배열) 연산도 지원
# Numpy에서 행렬은 2차원 배열로 표현

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# 덧셈연산
C = A + B
print(C)

# 뺄셈연산
D = A - B
print(D)

# 곱셈 연산
E = A * B
print(E)

# 나눗셈 연산
F = A / B
print(F)

# axis : 배열의 축을 나타내는 파라미터(매개변수). 2차원 이상의 다차원 배열에서 각 차원의 축 (axis)마다 연산을 수행할 수 있도록 지원
# 예 : axis = 0 : 행(row)방향   axis=1 : 열(column)방향

arr5 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# 행 방향(axis = 0)으로 합을 계산 , 열 방향 (axis = 1)
sum_by_column = np.sum(arr5, axis=0)

print()
print()
print(sum_by_column)
