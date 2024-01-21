# 1. 텍스트 파일 읽기

# 1) read() 메소드
# file.read(size)
# 파일로부터 데이터를 읽어오는 메소드

# file = open('/.input/hello.txt', 'rt')
#
# str = file.read()  # 파일 전체를 한 번에 읽어 들임
# print(str)
#
# file.close()

# read() 메소드를 통해 전체를 읽으려면 그 만큼의 메모리 공간을 필요
# 읽어야 할 파일이 크다면 일부만 읽어 들이는 작업을 반복하는 반복문을 사용하여
# 파일 전체를 읽도록 구현하는 것이 좋다.

# file = open('input/엄마돼지아기돼지.txt', 'rt')
#
# while True:
#     str = file.read(5)
#     if not str:
#         break
#     print(str, end='')
#
# file.close()
# fille.read(5)는 파일로 부터 최대 5글자를 읽어들임.
# 파일이 종료되어 더 이상 읽어 들일 글자가 없으면 빈 문자열('')을 읽어 들임.

# 2) readline() 메소드
# 텍스트 파일을 한 줄씩 읽어서 처리하는 메소드
# 파일이 종료되어 더 이상 읽어 들일 글자가 없으면 빈 문자열('')을 읽어 들임.
# 반복문을 이용해서 여러 번 읽어 들여야 파일 전체를 읽을 수 있다.

# print('readline 메소드')
# file = open('input/hello.txt', 'rt')
#
# while True:
#     str = file.readline()
#     if str == '':
#         break
#     print(str, end='')
#
# file.close()

# 3) readlines() 메소드
# 라인 line 하나가 아니라 전체 라인 lines를 모두 읽어 각 라인 line 단위로 리스트에 저장하는 메소드
print()
file = open('input/hello.txt', 'rt')

line_list = file.readlines()
print(line_list)

count = 0
for line in line_list:
    for str in line:
        print(str)
        if str == '다':
            count += 1

print(f'다는 {count}번 나왔습니다.')
