fruits = ['사과','수박']
count = 3   # 입력 가능한 횟수

# 문제 1. : count는 0이 되면 종료가된다. 종료가 되고 나서는 '5개 과일은 ... 입니다'가 출력이 되야 한다.
# 문제 2. : 만약 동일한 과일이 입력될 경우 '동일한 과일이 있습니다.'가 출력되고 count는 차감되지 않는다.
# 문제 3. : 만약 다른 과일이 입력된 경우 count가 차감된다. 그리고 차감된 이후 '입력이 ...번 남았습니다.' 라는 문구가 떠야 한다.

while count > 0:
    fruit = input('어떤 과일을 저장할까요? >>> ')
    # hint : 파이썬의 'in'을 구글에 검색해 찾아보시오.
    if fruit in fruits: # 리스트에 fruit 변수에 있는 값이 있다면
        print('동일한 과일이 있습니다.')
        continue # while문의 시작 지점으로 돌아가서 다시 과일 이름을 입력
    fruits.append(fruit)
    count -= 1
    print(f'입력이 {count}번 남았습니다.')

print(f'5개 과일은 {fruits}입니다.')