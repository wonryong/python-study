# 딕셔너리 dict
# 사전처럼 어떤 단어와 그 단어의 의미로 구성
# '키 key' 와 '값 value'를 '단어'와 '단어의 의미' 처럼 사용
# 딕셔너리는 인덱스가 존재하지 않는 대신 키를 인덱스처럼 사용
# 키 값을 알면 저장된 값을 확인할 수 있는 구조

d = {'a':'apple','b':'banana'} # {key:value, key:value}
print(d)
print(type(d)) #
print(d['a']) # 변수 d 딕셔너리에서 a라는 문자(문자열)을 찾겠다.
print(d['b'])

# 키값의 자료형이 문자열(str) 이라면 dict() 함수를 이용해서 생성 가능하다.

c = dict(a='apple',b='banana',c='candy')
print(c)

# 딕셔너리 요소의 추가와 삭제
# 새로운 키와 값을 조합해서 작성
print()
dic = {'apple':'사과'}
dic['watermelon'] = '멜론'
print(dic)

# 존재하는 키값을 이용해서 정의하면, value 수정으로 인식
dic['watermelon'] = '수박'
print(dic)

# setdefault() 메소드를 이용한 추가
me = {'name':'james'}
me.setdefault('age',20)
print(me)

# update() 메소드의 경우 존재하는 키값이면 수정
me.update(age=25)
print(me)

# update() 메소드의 경우 존재하지 않는 키값이면 추가
me.update(address='daegu')
print(me)

# pop() 메소드가 키값을 전달하면 해당 키값의 데이터가 삭제
me.pop('address')
print(me)