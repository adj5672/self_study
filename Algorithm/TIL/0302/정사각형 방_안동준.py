# 2차원 배열 DFS
def DFS(x,y):

    # 시작점이 방문하지 않았을 경우 이동거리를 계산한다.
    if visited[x][y] == 0:

        start = room[x][y]
        visited[x][y] = 1

        while True:
            for i in range(4):
                # 조건을 만족하면 이동
                if 0 <= x + dr[i] < N and 0 <= y + dc[i] < N and room[x+dr[i]][y+dc[i]] - room[x][y] == 1:
                    x, y = x + dr[i], y + dc[i]
                    visited[x][y] = 1
                    break
            # 더 이상 갈 곳이 없으면 도착방의 숫자 저장
            else:
                end = room[x][y]
                break
        # 최종적으로 방문한 방의 수
        return end - start + 1

    # 이미 방문한 방이 시작점일 경우,
    # 그 방의 최대 방문 가능 방의 수는 그 방을 처음 지나갔을 때의 방법보다 더 적을 수 밖에 없으므로 pass
    return 0

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # N * N 방
    N = int(input())

    # 방 정보
    room = []
    for _ in range(N):
        room.append(list(map(int,input().split())))

    # 델타 (상 좌 하 우)
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]

    max_visit, max_room = 0, N ** 2
    # 방문 배열
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # 시작점 (i, j)
    for i in range(N):
        for j in range(N):
            # 최대 방문 가능한 방의 수가 최대 방문 수보다 작으면 pass
            if N ** 2 - room[i][j] + 1 <= max_visit:
                pass
            # 최댓값 갱신 가능할 시 계산
            else:
                move = DFS(i,j)
                # 방문 수 비교
                if move > max_visit:
                    max_visit = move
                    max_room = room[i][j]
                # 최대 방문 수가 같은 경우 시작번호가 더 적은 숫자 선택
                elif move == max_visit and max_room > room[i][j]:
                    max_room = room[i][j]
    
    # 출력
    print('#{} {} {}'.format(test_case, max_room, max_visit))
