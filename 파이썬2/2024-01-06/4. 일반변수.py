# 일반변수

# num1 = 10
# num2 = 20
# print(num1)
# print(num2)

# 참조변수란 : 예) 변수 = 10 가정을 하면 이 10이 변수 안에다가 들어간다
# 참조변수는 10이라는게 변수 안에다가 들어가는 것이 아니라 10이라는 메모리 주소를 할당받는다.

class Score:

    # -> : 함수 리턴 값의 주석 역활을 한다.
    # 반환값이 없음, 값이 없음을 나타내는 특별한 값이다.
    def __init__(self, no: int) -> None:
        self.no = no

    def __str__(self) -> str:
        return str(self.no)

def print_hello() -> None:
    print("Hello World")

result = print_hello()
print(result)

#
# no1 = Score(1)
# no2 = Score(20)
# print(no1)
# print(no2)
#
# print(id(no1))
# print(id(no2))
#
# no1 = no2
# print(no1)
# print(no2)
#
# no2.no = 30
# print()
# print(no1)
# print(no2) # no1, no2는 참조변수라서 주소가 복사
# print(id(no1))
# print(id(no2))


# 일반 변수 : 일반 변수는 값을 직접 저장하고 해당 변수를 다른 변수에 할당할 때 값이 복사된다.
# 대표적으로 int형,부동소수점(float), 문자열(string), 불린(boolean)
a = 5
b = a
a = 10  # a를 변경해도 b는 영향을 받지 않음

# 참조 변수 : 데이터의 주소값을 저장한다. 여러 변수가 같은 데이터를 참조할 수 있다. 데이터의 크기가 가변적이며, 메모리에 데이터를 저장하고 그 데이터의 주소를 변수에 저장한다.
# 대표적으로 리스트(list),딕셔너리(dictionary), 객체(object) 등

list1 = [1, 2, 3]
list2 = list1  # list2가 list1을 참조
list1.append(4)  # list1에 원소 추가
print(list2)

