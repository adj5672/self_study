# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # N : 보드 한 변의 길이, M : 돌을 놓는 횟수
    N, M = map(int,input().split())

    # 오셀로 판 만들기 (1 : 흑돌, 2: 백돌)
    arr = [[0 for _ in range(N)] for _ in range(N)]
    arr[N // 2 - 1][N // 2], arr[N // 2][N // 2 - 1] = 1, 1
    arr[N // 2][N // 2], arr[N // 2 -1][N // 2 -1] = 2, 2

    # 돌 놓는 data
    data = []
    for _ in range(M):
        data.append(list(map(int,input().split())))

    # 돌 놓기
    for turn in data:
        # 돌의 위치, 돌의 색
        y, x, color = turn[0]-1, turn[1]-1, turn[2]
        # 돌 놓기
        arr[x][y] = color

        # 서쪽방향
        for i in range(-1, -N, -1):
            if 0 <= y + i < N:
                if arr[x][y+i] == 0:
                    break
                elif arr[x][y+i] == color:
                    for j in range(i,0):
                        arr[x][y+j] = color
                    break

        # 북서쪽
        for i in range(-1,-N,-1):
            if 0 <= x + i < N and 0 <= y + i < N:
                if arr[x+i][y+i] == 0:
                    break
                elif arr[x+i][y+i] == color:
                    for j in range(i,0):
                        arr[x+j][y+j] = color
                    break

        # 북쪽
        for i in range(-1,-N,-1):
            if 0 <= x + i < N:
                if arr[x+i][y] == 0:
                    break
                elif arr[x+i][y] == color:
                    for j in range(i,0):
                        arr[x+j][y] = color
                    break

        # 북동쪽
        for i in range(-1,-N,-1):
            if 0 <= x + i < N and 0 <= y - i < N:
                if arr[x+i][y-i] == 0:
                    break
                elif arr[x+i][y-i] == color:
                    for j in range(i,0):
                        arr[x+j][y-j] = color
                    break

        # 동쪽
        for i in range(1,N):
            if 0 <= y + i < N:
                if arr[x][y+i] == 0:
                    break
                elif arr[x][y+i] == color:
                    for j in range(0,i):
                        arr[x][y+j] = color
                    break

        # 남동쪽
        for i in range(1,N):
            if 0 <= x + i < N and 0 <= y + i < N:
                if arr[x+i][y+i] == 0:
                    break
                elif arr[x+i][y+i] == color:
                    for j in range(0,i):
                        arr[x+j][y+j] = color
                    break

        # 남쪽
        for i in range(1,N):
            if 0 <= x + i < N:
                if arr[x+i][y] == 0:
                    break
                elif arr[x+i][y] == color:
                    for j in range(0,i):
                        arr[x+j][y] = color
                    break

        # 남서쪽
        for i in range(1,N):
            if 0 <= x + i < N and 0 <= y - i < N:
                if arr[x+i][y-i] == 0:
                    break
                elif arr[x+i][y-i] == color:
                    for j in range(0,i):
                        arr[x+j][y-j] = color
                    break

    # 갯수 확인하기
    black, white = 0, 0
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 1:
                black += 1
            elif arr[x][y] == 2:
                white += 1

    # 출력
    print('#{} {} {}'.format(test_case, black, white))