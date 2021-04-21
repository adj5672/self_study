# node : 정점 번호, count : 경로의 길이
def DFS(node, count):
    global max_length

    visited[node] = 1
    count += 1

    # 최장 경로 길이 갱신
    if count > max_length:
        max_length = count

    # 각 정점마다
    for i in range(1, N + 1):
        # 인접해있고 방문하지 않았다면
        if adj[node][i] and not visited[i]:
            DFS(i, count)
            visited[i] = 0

# test_case 갯수
T = int(input())

for test_case in range(1, T + 1):
    # N : 정점의 갯수, M : 간선의 갯수
    N, M = map(int, input().split())

    # 인접행렬 정보
    adj = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u][v], adj[v][u] = 1, 1

    # 최장 경로 길이
    max_length = 0

    # 방문배열
    visited = [0 for _ in range(N + 1)]

    # 각 정점을 시작 정점으로 DFS 탐색
    for node in range(1, N + 1):
        DFS(node, 0)
        visited[node] = 0

    # 출력
    print('#{} {}'.format(test_case, max_length))