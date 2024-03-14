import sys

if __name__ == '__main__':



#     input = sys.stdin.readline

#     columns_maximum = []
#     for i in range(9):
#         temp = list(map(int, input().split()))
#         maximum = max(temp)
#         column_index = temp.index(maximum) + 1
#         columns_maximum.append((maximum, column_index))

#     column_maximum = columns_maximum[0][0]
#     maximum_low_index = 1  
#     maximum_column_index = columns_maximum[0][1]  

#     for i in range(1, 9):
#         if column_maximum < columns_maximum[i][0]: # 이렇게 하면 최대값이 여러 군데 있을 경우
#                                                    # 가장 처음에 발견된 최대값과 그 위치를 반환하게 되고 문제에 통과한다.
#             column_maximum = columns_maximum[i][0]
#             maximum_low_index = i + 1  
#             maximum_column_index = columns_maximum[i][1] 

#     print(column_maximum)
#     print(maximum_low_index, maximum_column_index)
    
#     input = sys.stdin.readline    

#     rows_maximum = []

#     for i in range(9):
#         temp = list(map(int, input().split()))
#         row_maximum = float('-inf')  
#         column_index = 0

#         for j, value in enumerate(temp):
#             if value >= row_maximum:
#                 row_maximum = value
#                 column_index = j + 1  
#         rows_maximum.append((row_maximum, column_index))

#     row_maximum = rows_maximum[0][0]
#     maximum_low_index = 1  
#     maximum_column_index = rows_maximum[0][1]  
    
#     for i in range(1, 9):
#         if row_maximum <= rows_maximum[i][0]:
#             row_maximum = rows_maximum[i][0]
#             maximum_low_index = i + 1  
#             maximum_column_index = rows_maximum[i][1] 

#     print(row_maximum)
#     print(maximum_low_index, maximum_column_index)



    input = sys.stdin.readline

    # 전체 격자판의 최댓값과 위치 초기화
    max_value = float('-inf')
    max_row = 0
    max_column = 0

    # 9x9 격자판 입력 받으며 바로 최댓값 찾기
    for i in range(9):
        row = list(map(int, input().split()))

        for j, value in enumerate(row):
            if value > max_value:
                max_value = value
                max_row = i + 1  # 1부터 시작하는 행 인덱스
                max_column = j + 1  # 1부터 시작하는 열 인덱스


    # 최댓값과 위치 출력
    print(max_value)
    print(max_row, max_column)