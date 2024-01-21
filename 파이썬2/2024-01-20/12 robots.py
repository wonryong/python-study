import requests

# 모든 크롤링이 불법은 아님
# 하지만 운영자의 의사에 상관없이 무단으로 크롤링 하는 것은 불법

# 운영자의 의사를 알 수 있는 방법
# robot.txt 에서 확인

# allow 는 허용
# disallow는 불가

urls = ['https://www.naver.com','https://ko.wikipedia.org']
filename = '/robots.txt'

for url in urls:
    file_path = url + filename
    print(file_path)
    resp = requests.get(file_path)
    print(resp.text)

