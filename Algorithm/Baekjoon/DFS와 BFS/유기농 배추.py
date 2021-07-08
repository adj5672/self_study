from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    arr = [[0 for _ in range(M)] for _ in range(N)]
    
    for _ in range(K):
        n, m = map(int, input().split())
        arr[m][n] = 1

    count = 0

    for x in range(N):
        for y in range(M):
            if arr[x][y]:
                count += 1
                queue = deque([[x, y]])
                while queue:
                    cur = queue.pop()
                    cur_x, cur_y = cur[0], cur[1]
                    arr[cur_x][cur_y] = 0
                    for i in range(4):
                        if 0 <= cur_x + dr[i] < N and 0 <= cur_y + dc[i] < M:
                            if arr[cur_x + dr[i]][cur_y + dc[i]] and [cur_x + dr[i], cur_y + dc[i]] not in queue:
                                queue.append([cur_x + dr[i], cur_y + dc[i]])

    print(count)