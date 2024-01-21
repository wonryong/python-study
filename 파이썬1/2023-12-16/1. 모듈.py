# 1. 모듈이란
# 모듈 module이란 한 마디로 파이썬 파일 (.py)
# 언제든지 사용할 수 있도록 변수나 함수 또는 클래스를 모아 놓은 파일

# 2. 모듈 생성
# converter.py 생성

# 3. 모듈의 사용
# 반드시 같은 디렉터리에(폴더) 있어야 한다.
# 모듈에 저장된 함수를 사용하는 방법
# 1. 모듈 전체를 가져오는 방법
# 모듈에 저장된 모든 클래스나 함수를 사용하고자 할 때
# 예) import 모듈

import converter

miles = converter.kilometer_to_miles(150)  # 모듈함수.함수() 형식으로 호출
print(f'150km = {miles}miles')  # 150km = 93.20565miles

pounds = converter.gram_to_pounds(1000)
print(f'1000g = {pounds}pounds')  # 1000g = 2.205pounds

# 2. 모듈에 포함된 함수 중에서 특정 함수만 골라서 가져오는 방법

# 예) from 모듈 import 함수
# 예) from 모듈 import 함수1, 함수2
# 예) from 모듈 import *

print()
from converter import kilometer_to_miles  # 모듈은 가져오지 않고 특정 함수만 가져온다.

miles = kilometer_to_miles(200)  # 모듈명을 명시하지 않고 사용
print(f'200km = {miles} miles')  # 200km = 124.27420000000001 miles

print()

from converter import *  # 모듈은 사용하지 않고 모듈의 모든 함수를 가져온다.

pounds = gram_to_pounds(10000)  # 모듈명을 명시하지 않고 사용
print(f'10000g = {pounds} pounds')  # 10000g = 22.05 pounds

# 4. 별명 사용하기
# 모듈이나 함수를 import 하는 경우에 원래 이름 대신 별명 alias 를 지정하고 사용
# 모듈이나 함수의 이름이 긴 경우에 주로 짧은 별명을 지정하고 긴 본래 이름 대신 사용
# 별명을 지정할 때는 as 키워드를 사용

print()

import converter as cvt  # converter 모듈에 cvt라는 별명을 지정

miles = cvt.kilometer_to_miles(150)  # 별명을 이용해서 함수 사용
print(f'150km = {miles}')  # 별명을 이용해서 함수 사용

pounds = cvt.gram_to_pounds(1000)
print(f'1000g = {pounds}')

print()

from converter import kilometer_to_miles as k_to_m  # 함수에도 별명을 지정가능

miles = k_to_m(150)  # 함수 이름 대신 별명을 사용
print(f'150km = {miles}')
