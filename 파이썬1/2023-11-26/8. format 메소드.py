# format() 메소드
# format() 메소드의 인수로 변수나 값을 표시하고, 해당 값이 표시될 위치를 중괄호({})로 표시하는 방식

print('My name is {}'.format('james'))
print('My name is {name}'.format(name='James'))

print('My name is {}. I\'m {} years old'.format('james',25))
print('My name is {0}. I\'m {1} years old'.format('james',25)) # 인덱스가 지정 가능하다.
print('My name is {1}. I\'m {0} years old'.format('james',25))
print('My name is {name}. I\'m {age} years old'.format(name='james',age=25))