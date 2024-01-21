class Car:
    max_oil = 50  # 최대 주유량

    def __init__(self, oil):
        self.oil = oil

    def add_oil(self, oil: int):
        if oil <= 0:  # 0 이하의 주유는 진행 X
            return
        self.oil += oil
        if self.oil > Car.max_oil:  # 주유 후 최대 주유량 초과 상태이면
            self.oil = Car.max_oil  # 현재 주유량을 최대 주유량으로 설정

    def car_info(self):
        print(f'현재 주유 상태: {self.oil}')


class Hybrid(Car):
    max_battery = 30

    def __init__(self, oil: int, battery: int):
        super().__init__(oil)
        self.battery = battery

    def charge(self, battery: int):
        if battery <= 0:
            return
        self.battery += battery
        if self.battery > Hybrid.max_battery:
            self.battery = Hybrid.max_battery

    def hybrid_info(self):
        super().car_info()
        print(f'현재 충전상태 : {self.battery}')

car = Hybrid(0,0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()

