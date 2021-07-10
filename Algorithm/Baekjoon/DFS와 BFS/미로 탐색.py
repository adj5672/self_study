from collections import deque

def BFS():
    queue = deque([[0, 0, 1]])
    visited[0][0] = 1
    while queue:
        cur = queue.popleft()
        x, y = cur[0], cur[1]
        if x == N - 1 and y == M - 1:
            return cur[2]
        for i in range(4):
            if 0 <= x + dr[i] < N and 0 <= y + dc[i] < M:
                if not visited[x + dr[i]][y + dc[i]] and arr[x + dr[i]][y + dc[i]]:
                    queue.append([x + dr[i], y + dc[i], cur[2] + 1])
                    visited[x + dr[i]][y + dc[i]] = 1


N, M = map(int, input().split())
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

arr = []
for _ in range(N):
    arr.append(list(map(int, list(input()))))
visited = [[0 for _ in range(M)] for _ in range(N)]

print(BFS())