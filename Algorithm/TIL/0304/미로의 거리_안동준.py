# BFS
def BFS(x,y):
    
    # 출발좌표 append 및 방문 표시
    queue.append([x,y])
    visited[x][y] = 1

    while queue:
        # cur : 현재 좌표
        cur = queue.pop(0)
        cur_x, cur_y = cur[0], cur[1]
        # 사방 탐색
        for i in range(4):
            # 이동할 곳이 인덱스 범위 내에 있고
            if 0 <= cur_x + dr[i] < N and 0 <= cur_y + dc[i] < N:
                # 벽이 아니며 방문하지 않았을 경우
                if maze[cur_x + dr[i]][cur_y + dc[i]] != 1 and visited[cur_x + dr[i]][cur_y + dc[i]] == 0:
                    # queue에 다음 칸 좌표 append 및 방문 표시(거리 저장)
                    queue.append([cur_x + dr[i],cur_y + dc[i]])
                    visited[cur_x + dr[i]][cur_y + dc[i]] = visited[cur_x][cur_y] + 1
                # 만약 도착 지점을 발견 했다면 함수 종료
                if maze[cur_x + dr[i]][cur_y + dc[i]] == 3:
                    return

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):

    # N : 미로의 크기
    N = int(input())

    # 미로
    maze = []
    for _ in range(N):
        maze.append(list(map(int,list(input()))))

    # 출발 지점과 도착 지점 찾기
    for x in range(N):
        for y in range(N):
            if maze[x][y] == 3:
                ex, ey = x, y
            elif maze[x][y] == 2:
                sx, sy = x, y

    # 방문 및 거리 배열
    visited = [[0 for _ in range(N)] for _ in range(N)]

    # 델타 (상 우 하 좌)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # BFS 함수 실행
    queue = []
    BFS(sx,sy)

    # 만약 도착지점에 도달 했다면 거리 반환
    if visited[ex][ey]:
        result = visited[ex][ey] - 2
    # 도달하지 않았다면 0
    else:
        result = 0

    # 출력
    print('#{} {}'.format(test_case, result))