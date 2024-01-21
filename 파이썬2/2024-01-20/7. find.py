import requests
from bs4 import BeautifulSoup as bs

# BeautifulSoup 실습 : find 메소드를 이용

# 1) find() 메소드
# 지정된 태그들 중에서 가장 첫 번째 태그만 가져오는 메소드.
# 일반적으로 하나의 태그만 존재하는 경웨 사용. 만약 여러 태그가 있으면 첫 번째 태그만 가져온다

# 위키피디아 '대구광역시' 페이지
url = 'https://ko.wikipedia.org/wiki/%EB%8C%80%EA%B5%AC%EA%B4%91%EC%97%AD%EC%8B%9C'
response = requests.get(url)
soup = bs(response.text,'html.parser')

first_img = soup.find(name='img') # img 태그 중에 제일 먼저 나온 것
print(type(first_img))
print(first_img)