# 생성자를 이용해서 용량을 가진 usb 인스턴스를 만드는 프로그램

class USB:

    def __init__(self,value):
        self.value = value

    def info(self):
        print(f'{self.value}GB USB')

usb = USB(128)
usb.info()
usb2 = USB(64)
usb2.info()