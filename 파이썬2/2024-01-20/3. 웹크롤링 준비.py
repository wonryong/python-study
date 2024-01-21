# 웹 크로링의 준비

# 1. 크롬 설치하기
# 크롬에 있는 '개발자 도구'를 수행할 때 필요한 정보를 확인

# 2. requests 라이브러리 설치하기
# pip install requests

# 사용자가 서버에 요청하는 것을 request (요청) 이라고 한다.
# requests 라이브러리는 쉽고 편리하게 request 를 처리할 수 있는 기능을 가지고 있다.

# 파이썬 표준 라이브러에는 request를 처리하기 위해서 urllib 라는 패키지가 있다.
# 대신 기능이 requests 라이브러리보다 못하다.

# 3. BeautifulSoup 패키지 설치
# pip install beautifulsoup4

# 구문을 통해 필요한 내용만 추출 할 수 있는 기능을 가지고 있는 외부 패키지

# 웹 크롤링은 어떤 식으로 돌아가냐?
# 웹 크롤링 web crawling 이란 완성된 웹 페이지에서 1) 필요한 정보를 수집 2) 선별하여 추출하는 과정을 의미

# 1. HTML의 구조
# 상위 요소와 하위 요소가 존재한다. (계층구조, 트리구조)
# <!doctype html> 은 HTML5임을 브라우저에게 알리는 선언
# 이후 <html> 태그부터 실제 HTML 태그 요소
# 전체 문서 내용은 <html></html> 사이에 처리되고 <html> 태그의 하위 요소로 <head> 태그와 <body> 태그가 있다.
# head 태그에는 한글처리를 위한 <meta>태그와 웹 페이지를 제목으로 사용하는 요소인 <title>태그가 포함
# body 태그의 하위 요소에는 제목 태그인 <h1>, 특정 구역을 나타낼 때 사용되는 <div> 태그가 포함

# 2. URL
# URL 이란 어떤 자원의 위치를 표기하는 방법이다.
#  구글에 접속하고 싶을 때는 웹 브라우저 주소 창에 https://www.google.co.kr/과 같은 인터넷 주소를 입력하는 것

# 프로토콜 : https: 하이퍼 텍스트 문서를 전송할 때 상용되는 프로토콜 (통신규약)
# 도메인 : naver.com
# 서브 도메인 : search.
# 파라미터 : ?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=코리아+it+아카데미









