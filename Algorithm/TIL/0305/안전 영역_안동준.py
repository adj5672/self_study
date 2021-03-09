# w : 수위, x,y : 좌표
def BFS(w,x,y):

    queue = []
    queue.append([x,y])
    visited[x][y] = 1

    while queue:
        
        cur = queue.pop(0)
        cur_x, cur_y = cur[0], cur[1]

        for i in range(4):
            if 0 <= cur_x + dr[i] < N and 0 <= cur_y + dc[i] < N:
                # 이동할 마을이 잠기지 않았고, 방문하지 않았다면 방문처리
                if arr[cur_x + dr[i]][cur_y + dc[i]] > w and visited[cur_x + dr[i]][cur_y + dc[i]] == 0:
                    queue.append([cur_x + dr[i], cur_y + dc[i]])
                    visited[cur_x + dr[i]][cur_y + dc[i]] = 1


# 마을 크기
N = int(input())

# 마을
arr = [list(map(int,input().split())) for _ in range(N)]

max_safe = 0

# 델타 (상 하 좌 우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 높이 i 만큼 비가 왔을 경우
for i in range(101):
    count = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if arr[x][y] > i and visited[x][y] == 0:
                BFS(i,x,y)
                count += 1
    if count > max_safe:
        max_safe = count

# 출력
print(max_safe)
