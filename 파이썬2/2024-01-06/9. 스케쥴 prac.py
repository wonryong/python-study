# 오늘의 스케쥴을 입력하면 그 내용이 모두 파일에 보관되는 프로그램이다.
# 스케줄을 입력하지 않고 enter 누르면 프로그램은 종료됩니다.
# 생성되는 파일의 이름은 현재 날짜이고 확장자는 txt입니다.
# '2024-01-06.txt'와 같은 형식을 갖추고 있습니다. // 참고 : 오늘은 1월 6일이지만 내일 실행을 할 때는 1월 7일이 찍히도록 해야 한다.
# hint : time 모듈을 불러오시오. // time.strftime 을 검색해 보고 사용하시오.

import time

file = open('./output/' + time.strftime('%Y-%m-%d') + '.txt', 'at', encoding='utf-8')

print('아무 것도 없게 될 시(아무것도 없는 상태에서 enter를 칠 시 종료)')
while True:
    schedule = input('오늘의 스케쥴을 입력하세요 >>> ')
    if not schedule:
        break
    file.write(schedule + '\n')

file.close()
