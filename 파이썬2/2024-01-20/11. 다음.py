import requests
from bs4 import BeautifulSoup as bs

# 다음 > 뉴스 > IT > 오늘의 연재의 첫 번째 글 제목과 신문사 들고오기.

url = 'https://news.daum.net/digital#1'
resp = requests.get(url)
soup = bs(resp.text,'html.parser')

# select : 여러 개의 요소를 선택 할 수 있다.
# select_one : 하나의 요소만 선택 가능
# .link_txt 를 입력하면 .은 클래스라는 뜻을 가지고 있다. .link_txt 는 class:link_txt 라고 알려준다.
tag_series = soup.select_one('.list_todayseries')
# print(tag_series)

tag_series_title = tag_series.select_one('.link_txt').text
print(f'제목 : {tag_series_title}')

tag_series_press = tag_series.select_one('.txt_info').text
print(f'신문사 : {tag_series_press}')