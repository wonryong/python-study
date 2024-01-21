# GUI란 무엇인가

# 파이썬의 GUI는 파이썬 언어를 사용하여 그래픽 사용자 인터페이스(GUI)를 만들 수 있는 라이브러리 프레임워크 모음이다.
# 이를 통해 사용자가 마우스 및 키보드와 같은 입력 장치를 사용하여 어플리케이션을 조작할 수 있다.
# 파이썬에서 가장 일반적으로 사용하는 GUI프레임워크는 Tkinter, PyQt, Pyside 등이 있다.

# 1)
import tkinter

# # 윈도우 창을 생성
# window = tkinter.Tk()
# # 윈도우 창을 종료시킬 때까지 실행시킨다.
# window.mainloop()

# # 2)
# # 윈도우 창을 생성
# window = tkinter.Tk()
# # 윈도우 창 이름 설정
# window.title('Test GUI')
# # 윈도우 창 크기와 위치 설정
# # (가로 x 세로 + x좌표 + y좌표) (문자열로도 받을 수 있다.)
# window.geometry('600x600+300+300')
# # 윈도우 창 크기 조절
# window.resizable(False, False)  # 첫 번째 False는 가로 조절, 두번째 False는 세로조절이다.
#
# window.mainloop()

# 3)

# Label : 파라미터로 전달한 윈도우에 라벨을 설정
# 라벨은 문자열, 형태, 상태, 하이라이트 색상 등 설정이 가능하다.

# window = tkinter.Tk()
# # 윈도우 창 이름 설정
# window.title('Test GUI')
# # 윈도우 창 크기와 위치 설정
# # (가로 x 세로 + x좌표 + y좌표) (문자열로도 받을 수 있다.)
# window.geometry('600x600+300+300')
# # 윈도우 창 크기 조절
# window.resizable(False, False)  # 첫 번째 False는 가로 조절, 두번째 False는 세로조절이다.
#
# label = tkinter.Label(window,text='파이썬',width=10,height=5,fg='blue',relief='solid')
# label.pack()
#
# window.mainloop()

# text : 라벨에 표시할 문자열
# textvariable : 라벨에 표시할 문자열을 가져올 변수
# anchor : 라벨안의 문자열 또는 이미지의 위치
# justift : 라벨의 문자열이 여러 줄일 경우 정렬을 해준다.
# wraplength : 자동 줄바꿈
# width : 라벨의 너비
# height : 라벨의 높이
# relief : 라벨의 테두리 모양
# background=bf : 라벨의 배경 색상
# fg : 글자 색상
# image : 라벨에 포함할 임의의 이미지
# font : 라벨의 문자열 글꼴 설정
# cursor : 라벨에 마우스를 올렸을 시 마우스 모양이 커서 모양이 된다.

# 4) Button
# 윈도우 창에 버튼 생성
# 옵션 중 command를 사용하여 사용자 정의 함수를 실행

import tkinter

count = 0

def countUP():
    global count
    count += 1
    label.config(text=str(count))


window = tkinter.Tk()
# 윈도우 창 이름 설정
window.title('Test GUI')
# 윈도우 창 크기와 위치 설정
# (가로 x 세로 + x좌표 + y좌표) (문자열로도 받을 수 있다.)
window.geometry('600x600+300+300')
# 윈도우 창 크기 조절
window.resizable(False, False)  # 첫 번째 False는 가로 조절, 두번째 False는 세로조절이다.

label = tkinter.Label(window, text='0')
label.pack()

button = tkinter.Button(window, overrelief='solid', width=15, command=countUP, repeatdelay=100000000, repeatinterval=1)

# repeatdelay : 버튼을 누르고 있는 상태로 유지했을 때, 명령이 반복되는 것이 활성화가 안된다. 예를 들어 누르면 0.1초마다 1개씩 증가하게 된다.
# repeatinterval : 버튼의 명령이 반복되서 호출되는 시간 간격을 밀리초 단위로 나타낸다.

button.pack()

window.mainloop()
