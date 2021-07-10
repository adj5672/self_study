from collections import deque

def BFS(x, y):

    n = 0
    queue = deque([[x, y]])
    while queue:
        cur = queue.popleft()
        n += 1
        i, j = cur[0], cur[1]
        arr[i][j] = 0
        for k in range(4):
            if 0 <= i + dr[k] < N and 0 <= j + dc[k] < N:
                if arr[i + dr[k]][j + dc[k]] and [i + dr[k], j + dc[k]] not in queue:
                    queue.append([i + dr[k], j + dc[k]])
    house.append(n)

N = int(input())
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

arr = [list(map(int, list(input()))) for _ in range(N)]

result, house = 0, []
for x in range(N):
    for y in range(N):
        if arr[x][y]:
            BFS(x, y)
            result += 1

print(result)
for h in sorted(house):
    print(h)