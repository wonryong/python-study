import requests
from bs4 import BeautifulSoup as bs

# select() 메소드
# CSS selector로 지정한 태그들을 모두 가져오는 메소드. 가져온 태그들은 모두 리스트에 복사

# CSS selector : 크롬 개발자 도구에서 1) 웹 페이지에서 마우스 우측 클릭 -> 검사
# 검사 창에서 원하는 위치에 마우스 우측 클릭 -> copy -> selector