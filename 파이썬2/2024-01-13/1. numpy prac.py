# 1. 주어진 2차원 배열에서 가장 큰값과 가장 작은 값을 찾는 NumPy 코드를 작성하시오
import numpy as np

arr = np.array([[3, 5, 1], [2, 9, 4]])

print(np.max(arr))
print(np.min(arr))

# 2. 주어진 1차원 배열의 요소들을 오름차순으로 정렬하는 NumPy 코드를 작성하시오.(구글에 찾아보시오.)

arr = np.array([9, 2, 7, 1, 5])
print(np.sort(arr))

# 3. 주어진 2차원 배열의 각 행에 대해 합계를 계산하는 NumPy코드를 작성하시오.

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.sum(arr, axis=0))

# 4. 주어진 2차원 배열의 각 열에 대해 합계를 계산하는 NumPy코드를 작성하시오.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.sum(arr, axis=1))

# 5. 주어진 1차원 배열의 요소 중에서 3보다 큰 값들만 선택하는 NumPy코드를 작성하시오.

arr = np.array([1, 4, 2, 5, 3, 6])

print(arr[arr > 3])

