from collections import deque

def DFS(node):
    visited[node] = 1
    print(node, end=' ')
    for i in range(1, N+1):
        if not visited[i] and adj[node][i]:
            DFS(i)

def BFS(node):

    queue = deque([node])
    visited[node] = 1

    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        for i in range(1, N+1):
            if not visited[i] and adj[cur][i]:
                queue.append(i)
                visited[i] = 1

N, M, V = map(int, input().split())

adj = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    n, m = map(int, input().split())
    adj[n][m] = adj[m][n] = 1

visited = [0 for _ in range(N+1)]
DFS(V)
print('')
visited = [0 for _ in range(N+1)]
BFS(V)
