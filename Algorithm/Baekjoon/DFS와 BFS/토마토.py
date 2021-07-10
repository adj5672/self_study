from collections import deque

def result():
    value = 0
    for x in range(N):
        for y in range(M):
            if not arr[x][y]:
                return -1
            if arr[x][y] > value:
                value = arr[x][y]
    return value - 1

def BFS(tomatos):
    queue = deque(tomatos)
    while queue:
        cur = queue.popleft()
        i, j = cur[0], cur[1]
        for k in range(4):
            if 0 <= i + dr[k] < N and 0 <= j + dc[k] < M:
                if arr[i + dr[k]][j + dc[k]] != -1 and not visited[i + dr[k]][j + dc[k]]:
                    queue.append([i + dr[k], j + dc[k]])
                    arr[i + dr[k]][j + dc[k]] = arr[i][j] + 1
                    visited[i + dr[k]][j + dc[k]] = 1

M, N = map(int, input().split())
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

arr = [list(map(int, input().split())) for _ in range(N)]

tomatos = []
visited = [[0 for _ in range(M)] for _ in range(N)]
for x in range(N):
    for y in range(M):
        if arr[x][y] == 1:
            tomatos.append([x, y])
            visited[x][y] = 1
BFS(tomatos)

print(result())