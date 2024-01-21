
# 섭씨를 화씨로 변환한 함수
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 /5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius