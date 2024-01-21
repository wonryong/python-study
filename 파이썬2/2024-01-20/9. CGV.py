import requests
from bs4 import BeautifulSoup as bs

# CGV 무비차트에서 순위별로 영화 제목 들고오기

url = 'http://www.cgv.co.kr/movies/'
resp = requests.get(url)
soup = bs(resp.text,'html.parser')

tags = soup.select('#contents > div.wrap-movie-chart > div.sect-movie-chart > ol > li > div.box-contents > a > strong')

# ol:nth-child(2) : ol 태그가 많은데 그 중에서 2번째 ol태그를 선택한다.
# li:nth-child(1) : li 태그 중에서 첫 번째 태그를 보겠다.

for idx, tag in enumerate(tags):
    print(str(idx + 1), tag.text)