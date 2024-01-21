# 문제

# 한 가게에서 고객의 주문을 처리하는 프로그램을 작성하려 한다. 사용자로부터 주문한 제품의 가격과 수량을 입력 받아서 총 주문 가격을 계산하는 프로그램을 작성하려고 한다. 그러나 다음과 같은 상황들은 예외 처리해야한다.

# 1. 가격과 수량을 입력할 때 숫자가 아닌 값이 입력되면 "올바른 숫자를 입력하세요." 라는 메시지가 나와야 한다.

# 2. 가격이 음수인 경우 "가격은 음수일 수 없습니다."라는 메시지가 나와야 한다.
# 3. 수량이 음수인 경우 "수량은 음수일 수 없습니다."라는 메시지가 나와야 한다.

# try:
#     price = float(input('제품의 가격을 입력하세요 >>>'))
#     quantity = int(input("제품의 수량을 입력하세요 >> "))
#
#     if price < 0:
#         raise ValueError("가격은 음수일 수 없습니다.")
#     if quantity < 0:
#         raise ValueError("수량은 음수일 수 없습니다.")
#
#     total_price = price * quantity
#     print("총 주문 가격은 : ", total_price)
#
# except ValueError as e:
#     print(e)
#
# except Exception as e:
#     # 그 외의 예외 상황에 대한 예외 처리
#     print("오류 발생", e)

# try:
#     price = float(input('제품의 가격을 입력하세요: '))
#     quantity = int(input('제품의 수량을 입력하세요: '))
#
#     if price < 0:
#         raise ValueError('가격은 음수일 수 없습니다.')
#     if quantity < 0:
#         raise ValueError('수량은 음수일 수 없습니다.')
#
# except ValueError:
#     print('올바른 숫자를 입력하세요')
#
# except Exception as e:
#     print('오류 발생', e)




# try:
#     price = float(input('제품의 가격을 입력하세요: '))
#     quantity = int(input('제품의 수량을 입력하세요: '))
#
#     if price < 0 or quantity < 0:
#         print('가격과 수량은 음수일 수 없습니다.')
#     else:
#         total_price = price * quantity
#         print('총 주문 가격은:', total_price)
#
# except ValueError:
#     print('올바른 숫자를 입력하세요.')
#
# except Exception as e:
#     print('오류 발생', e)

