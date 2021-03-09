# 2차원 배열 DFS
def DFS(x,y,end_x,end_y):

    if x == end_x and y == end_y:
        return 1

    visit[x][y] = 1

    for i in range(4):
        if 0 <= x + dr[i] < N and 0 <= y + dc[i] < N and maze[x+dr[i]][y+dc[i]] != 1 and visit[x+dr[i]][y+dc[i]] == 0:
            if DFS(x+dr[i],y+dc[i],end_x,end_y) == 1:
                return 1
    else:
        return 0

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # N * N 미로
    N = int(input())

    # 미로
    maze = []
    for _ in range(N):
        maze.append(list(map(int,list(input()))))

    # 출발점, 도착점
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                s_x, s_y = i, j
                break
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                e_x, e_y = i, j
                break

    # 델타 (상 좌 하 우)
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]

    # 방문 배열
    visit = [[0 for _ in range(N)] for _ in range(N)]

    # 결과
    result = DFS(s_x,s_y,e_x,e_y)

    # 출력
    print('#{} {}'.format(test_case, result))