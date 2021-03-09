# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # N * N 2차원 배열
    N = int(input())
    room =[[0 for _ in range(N)] for _ in range(N)]

    # 델타
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    i = 0

    # x행 y열
    x, y, num = 0, 0, 2
    room[0][0] = 1

    while num <= N ** 2:
        # 다음 숫자가 들어갈 좌표가 인덱스 범위 내에 있고 그 좌표에 숫자가 채워져 있지 않으면 (0이 아니면)
        if 0 <= x + dr[i % 4] < N and 0 <= y + dc[i % 4] < N and not room[x + dr[i % 4]][y + dc[i % 4]]:
            # 새로운 좌표 설정 및 숫자 대입
            x, y = x + dr[i % 4], y + dc[i % 4]
            room[x][y] = num
            num += 1
        # if 조건문을 만족하지 못하면 방향 전환
        else:
            i += 1
    
    # 출력
    print('#{}'.format(test_case))
    for row in room:
        print(' '.join(map(str,row)))