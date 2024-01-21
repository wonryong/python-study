# 파이썬에서 데이터를 효과적으로 시각화하기 위해 만든 라이브러리
# matplotlib은 MATLB(과학 및 공학 연산을 위한 소프트웨어)의 시각화 기능을 모델링해서 만들어졌다

# 공식 홈페이지 : https://matplotlib.org

import matplotlib.pyplot as plt

# 1. 선 그래프
# 1) 기본적인 선 그래프 그리기
# 선 그래프는 그래프 중 가장 기본이 되는 그래프.
# 순서가 있는 숫자 데이터를 시각화하거나 시간에 따라 변하는 숫자 데이터를 시각화 하는데 많이 사용

# 기본 형식 : plt.plot([x, ]y[, fmt])
# x와 y는 각각 x축과 y축 좌표의 값을 의미
# x와 y는 시퀀스 길이가 같아야 한다.
# x와 y 데이터 중에서 x는 생략이 가능하다. x가 없다면 x는 0부터 y의 개수만큼 1씩 증가하는 값으로 자동 할당
# fmt는 format string으로 다양한 형식으로 그래프를 그릴수 있는 옵션

# x축 데이터를 지정하지 않고, y축 데이터만 있는 경우
# 숫자로 이루어진 리스트 데이터 생성
# data1 = [10,14,19,20,25]
# plt.plot(data1)
# print(data1)
# plt.show()  # 그래프가 출력되려면 show() 실행.

# x값과 y값이 모두 있는 데이터
import numpy as np

x = np.arange(-4.5, 5, 0.5) # 배열 x 생성 범위 : [-4.5 ~ 5] 0.5씩 증가
y = 2 * x **2 # : x를 제곱한 후에 그 결과에 2를 곱한 것이다.
print(x,y)
plt.plot([x,y])
plt.show()

# 그래프 제목, 행 , 열에다가 주석(라벨)을 설정할 수 있다. (그래프 색깔도 변경 가능)
data2 = [10,14,19,20,25]
plt.plot(data2, color='red')  # 색깔지정
plt.title("Data2") # 위의 제목에 글자를 새겨준다.
plt.xlabel("This is x") # x축에다가 글자를새긴다
plt.ylabel('This is y') # y축에다가 글자를 새긴다
plt.show()

