import requests
from bs4 import BeautifulSoup as bs

# BeautifulSoup : 구문을 분석해서 필요한 내용만 추출할 수 있는 기능을 가진 외부 패키지

url = 'https://ko.wikipedia.org/wiki/%EB%8C%80%EA%B5%AC%EA%B4%91%EC%97%AD%EC%8B%9C'
response = requests.get(url)
soup = bs(response.text,'html.parser')
# parser란 주로 문자열 데이터를 분석하고 이를 다른 형태의 자료 구조로 변환하는 프로그램을 뜻한다.
# print(soup)
print(soup.find('title'))