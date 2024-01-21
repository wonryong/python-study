# enumerate() : 리스트에 저장된 요소와 해당 요소의 인덱스가 튜플 형태로 함께 추출
# for item in enumerate([리스트])
# 반복실행문

for item in enumerate(['가위','바위','보']):
    print(item)

for idx, element in enumerate(['가위','바위','보']):
    print(idx,'/',element)

# range() : 전달된 인수값에 따라 시퀀스 자료형의 데이터를 생성
# 1) range(stop) / 0 부터 stop 사이의 모든 정수가 생성. 생성되는 정수를 n이라고 하면 n의 범위는    0 <= n < stop

# 2) range(start, stop) / start부터 stop 사이의 모든 정수가 생성. 생성되는 정수를 n이라고 하면 n의 범위는 start <= n <stop

# 3) range(start,stop,step) start부터 stop 사의의 정수 중에서 step만큼의 차이를 가지고 있다.

print()
print(list(range(10)))
print(list(range(1, 11)))
print(list(range(0,30,5)))
print(list(range(0,10,3)))
print(list(range(0, -10, -1)))
print(list(range(0)))
print(list(range(1,0)))

# len() : 함수에 전달된 객체의 길이(항목 수)를 반환
print()
li = ['a','b','c','d']
print(len(li))

d = {'a':'apple','b':'banana'}
print(len(d)) # 2 / 딕셔너리는 '키:값'으로 구성된 한 쌍을 하나의 데이터로 본다

print(len(range(10)))
print(len(range(1,10)))

# range() 함수와 리스트의 길이를 구하는 len() 함수를 함께 사용하면 리스트의 인덱스를 생성 가능

seasons = ['봄','여름','가을','겨울']
seasons_eng = ['spring','summer','fall','winter']

# len(seasons) = 지금은 4를 집어넣는것과 같다.
for idx in range(len(seasons)):
    print(f'{seasons[idx]} / {seasons_eng[idx]}')

# sorted(): 전달된 반복가능객체의 오름차순 정렬 결과를 반환
# reverse=True : 옵션을 추가할 경우 내림차순 정렬 결과를 반환

print()
my_list2 = ['b','c','a','d']
print(sorted(my_list2))

my_list = [6,3,1,2,5,4]
print(sorted(my_list))
print(sorted(my_list,reverse=True))

# zip() : 전달된 여러 개의 반복가능객체의 각 요소를 튜플로 묶어서 반환
# 전달된 반복가능객체들의 길이가 서로 다르면 길이가 짧은 반복가능객체 기준으로 동작
print()

names = ['james','emily','amanda']
scores = [60,70,80]
for student in zip(names,scores):
    print(student)

# 튜플은 언패킹이 가능하므로 다음과 같은 모습으로 구성 가능

for name, score in zip(names,scores):
    print(f'{name}의 점수는 {score}입니다.')

for a ,b in zip(seasons,seasons_eng):
    print(f'{a}의 계절은 {b}입니다.')



