import urllib.request as request

# 크롤링 할 때 url을 이용해서 html을 가져오는 방법은 크게 2가지
# 1) 내장 모듈인 urllib를 사용
# 2) 외장 모듈인 requests를 사용
# 2번이 월등하게 좋다

# 정상접속
url = 'https://www.python.org'
code = request.urlopen(url)
print(code)

# 비정상 접속. 비정상일 경우 에러 발생
url = 'https://www.python.org/1'
code = request.urlopen(url)
print(code)

# 100 번대 : 요청은 처리되었으니 계속 진행해라
# 200 번대 : 성공
# 300 번대 : 리다이렉션 : 추가동작이 필요한 상태 ex) 요청한 URL의 웹 문서가 이동되었으니 그 주소로 다시 시해
# 400 번대 : 클라이언트 에러 : 요청을 받지 못했을 경우.
# 500 번대 : 서버 오류