# CSV
# 파이썬의 csv 모듈로 CSV 파일을 쉽게 구문 분석 가능.

# 장점
# 단순하다.
# 많은 프로그램에서 지원을 하고(Python, Visual code, Eclipse), 텍스트 편집기에서 볼 수 잇으며, 스프레드 시트 데이터를 표현하는 간단한 방법


# 단점
# 값에 유형이 없음. 모든 것은 다 문자열
# 글꼴 크기나 색상을 설정 X
# 여러 개의 워크시트를 가질 수 없다.
# 셀의 너비나 높이를 지정 X
# 그림이나 차트를 포함 X

# 1. reader 객체
# csv 모듈은 별도의 설치 X
import csv

# csv 모듈을 사용해서 csv 파일을 읽으려면 다른 테긋트 파일처럼 open() 함수로 파일을 읽어야 한다.
# example_file = open('./input/회원명단.csv')
#
# # read() 대신 csv.reader() 함수에 전달. reader() 객체가 반환
#
# example_reader = csv.reader(example_file)
#
# # list로 변환하여 값에 접근
# print(example_reader)
# example_data = list(example_reader)
# print(example_data)
# print(example_data[1][1])
# example_file.close()

# 2. for 반복문을 활용해 reader 객체로부터 데이터 읽기
# CSV 파일이 큰 경우에는, 전체 파일을 한 번에 메모리에 로드하지 않고
# for 반복문에서 reader 객체 사용
# example_file = open('./input/학생명단.csv')
# example_reader = csv.reader(example_file)
# print('example.csv 출력')
#
# for row in example_reader:
#     print(f'{str(example_reader.line_num)}{str(row)}{str(row[0])}')

# 4. 키보드 인자 delimiter와 lineterminator
# delimiter : 구분자, 설명해서 넘어감
# lineterminator : 끝문자
# 셀들이 탭으로 구분되어 있으면 탭으 구분된 값을 의미하는 .tsv 파일 확장자를 사용

# csv_file = open('./output/example.tsv', 'w', newline='')
# csv_writer = csv.writer(csv_file, delimiter='\t', lineterminator='\n\n')
# csv_writer.writerow(['apples', 'oranges', 'grapes'])
# csv_writer.writerow(['eggs', 'bacon', 'ham'])
# csv_writer.writerow(['spam', 'spam', 'spam', 'spam', 'spam'])
# csv_file.close()
# print('example 파일이 생성되었습니다.')

# 5. CSV 객체의 DictReader 와 DictWriter
# 헤더 행이 있는 CSV 파일의 경우 reader나 writer 객체보다
# DictReader나 DictWriter 객체를 사용하는 것이 작업하기 편하다.
# example_file = open('./input/example_with_header.csv')
# example_dict_reader = csv.DictReader(example_file)
# # DictReader 는 row 딕셔너리 객체로 설정하고, 첫 번째 행에 있는 정보를 건너뜀
# print('example_with_header.csv 출력')
# for row in example_dict_reader:
#     print(f'{row['Timestamp']},{row['Fruit']},{row['Quantity']}')

# Dictwriter 객체는 csv 파일을 생성하기 위해 딕셔너리를 사용
output_file = open('./output/output_with_header.csv', 'w', newline='')
output_dict_writer = csv.DictWriter(output_file, ['Name', 'Pet', 'Phone'])
# 파일에 헤더 행을 넣고 싶으면 writeheader()를 호출
output_dict_writer.writeheader()
# writerow() 메서드를 호출하여 각 행을 쓸 수 있는데 이 때 딕셔너리를 사용
# 딕셔너리의 키는 헤어디고, 딕셔너리의 값은 파일에 쓰려는 데이터가 들어간다.
output_dict_writer.writerow({'Name': 'Alice', 'Pet': 'Cat', 'Phone': '555-1234'})
# 누락된 키는 빈 상태로 나옴
output_dict_writer.writerow({'Name': 'Bob', 'Phone': '555-9999'})
output_dict_writer.writerow({'Phone': '555-5555', 'Name': 'Daniel', 'Pet': 'dog'})
# 순서는 중요하지 않다.
output_file.close()

import csv

