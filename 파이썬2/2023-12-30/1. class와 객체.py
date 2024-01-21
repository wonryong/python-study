# 1. 객체의 개념
# 개발을 하다 보면 정수나 실수 또는 문자열 등 기본적인 자료형으로 표현하기 힘든 것들이 존재
# 예를 들어 어떤 게시글을 파이썬으로 표현을 한다면
# 게시글 번호, 제목, 작성자, 비밀번호, 내용, 최초작성일자, 최종수정일자, 조회수가 필요.
# 이를 손쉽게 관리 하려면 8개의 항목을 하나의 이름을 가진 객체(object)로 만들어서 사용하는 것이 좋다.

# 2. 클래스의 개념
# 클래스 class를 한 마디로 정의하면 객체를 만드는 도구
# 하나의 클래스를 만들어 두면 그 클래스를 통해서 (동일한 구조를 가진) 여러 개의 객체를 만들 수 있다.
# 같은 클래스로 만든 객체라 하더라도 객체들은 서로 다른 값을 가질 수 있다.
# 인스턴스 instance 역시 클래스를 이용해서 생성한 객체를 가리키는 용어

# 객체와 인스턴스의 미묘한 차이
# 1) 와플머신 클래스로 만든 와플은 객체 object
# 2) 와플은 와플머신 클래스의 인스턴스 instance

# 3. 클래스 정의
# 클래스 정의 방법
# 1) class 키워드로 클래스를 정의
# 클래스 이름은 Upper Camel Case 규칙을 따름.
# 파이썬은 변수나 함수의 이름을 정할때 언더바 (_) 를 이용해 단어를 연결하는 Snake Case 방식을 사용하지만
# 클래스는 Upper Camel Case 규칙을 따름.
# print + member : printmember  1) print_member 2) printMember 3)PrintMember

# 클래스는 다음과 같은 형식으로 정의
# class 클래스:
# 본문

# 4. 객체 생성
# 클래스가 정의되었다면 다음과 같은 형식으로 객체를 생성
# 객체 = 클래스()

# 2개의 객체를 만들고 싶으면
# 객체1 = 클래스()
# 객체2 = 클래스()

# 5. 클래스 정의와 객체 생성
class WaffleMachine: # WaffleMachine 이라는 클래스 정의
    pass

waffle1 = WaffleMachine() # WaffleMachine 이라는 클래스를 이용해 waffle 이라는 객체 생성
waffle2 = WaffleMachine()

print(waffle1) # <__main__.WaffleMachine object at 0x000002088D48FAD0> : 메모리의 0x000002088D48FAD0 번지에 저장된 WaffleMachine의 객체라는 의미
print(waffle2)
