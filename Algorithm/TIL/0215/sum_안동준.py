for _ in range(10):
    test_case = int(input())
    # 100 * 100 2차원 배열만들기
    square = []
    for _ in range(100):
        square.append(list(map(int,input().split())))
    # max_value : 합의 최댓값
    max_value = 0

    # 행의 합 구하기
    for row in square:
        sum_value = 0
        # 각 행의 합 구하기
        for num in row:
            sum_value += num
        # 최댓값과 비교
        if sum_value > max_value:
            max_value = sum_value

    # 열의 합 구하기
    for j in range(100):
        sum_value = 0
        # 각 열의 합 구하기
        for row in square:
            sum_value += row[j]
        # 최댓값과 비교
        if sum_value > max_value:
            max_value = sum_value

    # 대각선의 합 구하기(오른쪽 아래 방향 대각선)
    cross_value1 = 0
    for i in range(100):
        cross_value1 += square[i][i]
    if cross_value1 > max_value:
        max_value = cross_value1

    # 대각선의 합 구하기(왼쪽 아래 방향 대각선)
    cross_value2 = 0
    for i in range(100):
        cross_value2 += square[i][99-i]
    if cross_value2 > max_value:
        max_value = cross_value2

    # 출력
    print('#{} {}'.format(test_case,max_value))