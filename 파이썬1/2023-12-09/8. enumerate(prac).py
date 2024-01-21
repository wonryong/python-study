# rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'pruple']
#
# for b, c in enumerate(rainbow):
#     print(f'무지개의 {b+1}번째 색은 {c}입니다')
#
#
#
# a = [1,2,3,4,5,6,7]
# b = ['red','orange','yellow','green','blue','navy','pruple']
#
# for a, b in zip(a, b):
#     print(f'무지개의 {a}번째 색은 {b}입니다.')


exam = []

print('점수를 입력하세요')
print('더 이상 점수가 없으면 음수를 아무거나 입력하세요.')
while True:
    score = int(input('점수를 입력하세요 >> '))
    if score < 0:
        break
    else:
        exam.append(score)

a = sum(exam) / len(exam)
b = max(exam)
c = min(exam)
print(f'평균 = {a}, 최대 = {b}, 최소 = {c}')