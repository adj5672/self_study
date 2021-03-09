# DFS
def DFS(x,y):

    visited[x][y] = 1

    for i in range(4):
        if maze[x+dr[i]][y+dc[i]] != 1 and visited[x+dr[i]][y+dc[i]] == 0:
            DFS(x+dr[i], y+dc[i])

# test_case 갯수 10개
for _ in range(10):
    # test_case 번호
    test_case = int(input())

    # 16 * 16 미로
    maze = []
    for _ in range(16):
        maze.append(list(map(int,list(input()))))

    # 출발 지점 도착 지점 찾기
    for x in range(16):
        for y in range(16):
            if maze[x][y] == 2:
                sx, sy = x, y
            elif maze[x][y] == 3:
                ex, ey = x, y

    # 방문 배열
    visited = [[0 for _ in range(16)] for _ in range(16)]

    # 델타 (상 우 하 좌)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # DFS 함수 실행
    DFS(sx,sy)
    
    # 출력
    print('#{} {}'.format(test_case, visited[ex][ey]))