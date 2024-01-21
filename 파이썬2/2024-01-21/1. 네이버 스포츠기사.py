import requests
from bs4 import BeautifulSoup as bs

# find_all() : 모든 요소를 출력

url = 'https://sports.news.naver.com/index'
response = requests.get(url)
soup = bs(response.text, 'html.parser')

today_list = soup.find('ul', {'class': 'today_list'}).find_all('strong')
for i in today_list:
    print(i.text)
