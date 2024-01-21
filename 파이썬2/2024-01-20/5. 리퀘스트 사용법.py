import requests

# Request : 클라이언트(유저가) 서버에 요청하는 메시지

# Response : 서버가 클라이언트(유저)에게 보내는 응답 메시지

# requests 사용법

url = 'https://naver.com'
response = requests.get(url) # get() 또는 (post) 메소드를 이용해서 html 정보를 받아온다.

html = response.text # response 객체의 text 속성을 지정하면 html 정보 반환

headers = response.headers # response 객체의 headers 속성을 지정하면 헤더 정보 반환
print(headers)
print(type(headers))
# 서버에서 헤더 정보가 JSON 타입 형식으로 들어온다.