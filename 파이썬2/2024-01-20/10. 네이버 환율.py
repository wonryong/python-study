import requests
from bs4 import BeautifulSoup as bs

# 네이버 환율 크롤링
# 네이버에서 '환율' 검색 후 환율 더 보기 클릭

url = 'https://finance.naver.com/marketindex/'
resp = requests.get(url)
soup = bs(resp.text,'html.parser')

nation = soup.select('#exchangeList > li > a > h3 > span')
print(nation)

exchange_rate = soup.select('#exchangeList > li > a > div > span.value')
print(exchange_rate)

for idx, item in enumerate(nation):
    print(f'{item.text} : {exchange_rate[idx].text}')