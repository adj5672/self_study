# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # 스도쿠 받아오기
    arr = []
    for _ in range(9):
        arr.append(list(map(int,input().split())))

    result = 1

    # 행 방향 확인하기
    for row in arr:
        # 각 행마다 합을 확인하여 45가 아니라면 result = 0
        r_sum = 0
        for num in row:
            r_sum += num
        if r_sum != 45:
            result = 0
            break
            
    # 열 방향 확인하기
    for col in range(9):
        # 이미 오류가 존재하면 break
        if not result:
            break
        # 각 열마다 합을 확인하여 45가 아니라면 result = 1
        c_sum = 0
        for row in range(9):
            c_sum += arr[row][col]
        if c_sum != 45:
            result = 0
            break

    # 3 * 3 확인하기
    for r_idx, row in enumerate(arr):
        # 이미 오류가 존재하면 break
        if not result:
            break
        # 3의 배수 행마다 배열 초기화
        if r_idx % 3 == 0:
            # 0~2 열의 합, 3~5 열의 합, 6~8 열의 합
            square = [0, 0 ,0]
        # 각 열에서 해당하는 square index 에 요소를 합한다.
        for c_idx, col in enumerate(row):
            square[c_idx // 3] += col
        # 만약 각 블럭의 합이 45가 아니라면 result = 1
        if r_idx % 3 == 2 and square != [45, 45, 45]:
            result = 0
            break

    # 출력
    print('#{} {}'.format(test_case, result))