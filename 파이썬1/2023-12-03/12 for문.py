# 1. 세트 set
# 비시퀀스 자료형이기 때문에 저장된 요소들 사이에 순서가 없음

# 기본 형식
# for 요소 in {세트}
# 반복실행

for item in {'가위','바위','보'}:
    print(item)

# 2. 딕셔너리
# key와 value의 조합이라 다른 자료형과 다른 방식으로 사용을 한다.
# 키만 출력
print()

person = {'name' : '에밀리','age' : 20, '주소' : '대구'}
for item in person:
    print(item)

print()

# value 출력
for key, value in person.items(): # 이걸 추천
    print(f'{key} : {value}')

print()

for key in person:
    print(f'{person[key]}')

print()

for key in person: # get() 메소드를 이용해서 해당 key에 해당하는 value를 가져온다.
    print(f'{person.get(key)}')
