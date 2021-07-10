def DFS(node):

    global result

    visited[node] = 1
    result += 1
    for i in range(N):
        if not visited[i] and adj[node][i]:
            DFS(i)

N = int(input())
M = int(input())

adj = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    n, m = map(int, input().split())
    adj[n-1][m-1] = adj[m-1][n-1] = 1

result = -1
visited = [0 for _ in range(N)]

DFS(0)
print(result)