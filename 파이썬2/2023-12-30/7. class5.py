class MyClass:
    # self : 특별한 예약어. 클래스의 인스턴스 메서드 안에서 사용된다.
    # 해당 메서드가 호출된 인스턴스를 가리킨다. self는 클래스 MyClass를 뜻한다.
    # 생성자(__init__) : 클래스가 만들어질때 무조건적으로 실행되는 함수
    # self.value = MyClass의 값
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)


obj = MyClass(42)

obj.print_value()


# 클래스를 선언
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name # 인스턴스 변수
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science # 메서드

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self,name):
        return f'{self.name}\t{self.get_sum()}\t    {self.get_average()}'



students = [
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

# 학생을 한 명씩 반복
print("이름", "총점", "평균", sep="\t\t")
for student in students:
    print(student.to_string(123))
