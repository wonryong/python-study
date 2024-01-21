# 변수 variable : 어떤 데이터를 저장하고자 할 때 사용하는 메모리 저장소

# 변수명 생성규칙
# 1. 영문, 한글, 숫자, 언더바(_)로 구성
# 2. 특수문자는 사용이 안된다.
# 3. 대소문자는 구분이 된다. 예) number와 Number는 다른 변수로 취급
# 4. 변수명의 첫 글자는 숫자를 사용할 수 없음 my2002(o) / 2002my(x)
# 5. 키워드(list, dict, if, for, and)등은 사용할 수 없음

# 권장하는 변수명
# 1. 가급적 영문 소문자로 작성
# 2. 한글을 사용하지 않고 영어 변수명 사용
# 3. 변수명으로 저장된 데이터 유추가 가능하도록 사용


name = 'Alice'
age = 25
address = '''우편번호 12345
서울시 영등포구 여의도동
서울빌딩501호'''  # multiple line 문자열 저장
boyfriend = None  # 아무것도 저장하지 않음 / 다른언어 : null / 파이썬은 None 이라고 표현
height = 170.5  # 실수를 저장

print(name)
print(age)
print(address)
print(boyfriend)
print(height)
