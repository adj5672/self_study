def DFS(s_node, e_node, visited, total_cost, max_cost):
    
    global result
    
    # 비용을 초과한 경우 return
    if total_cost > C:
        return

    # 이미 최소 비용을 초과한 경우
    if max_cost >= result:
        return

    # 도착한 경우
    if s_node == e_node:
        if max_cost < result:
            result = max_cost
        return

    # 방문처리
    visited[s_node] = 1
    for i in range(N):
        # 방문하지 않은 s_node에 인접한 교차로이면
        if not visited[i] and adj[s_node][i] < 1001:
            DFS(i, e_node, visited, total_cost + adj[s_node][i], max([max_cost, adj[s_node][i]]))
    visited[s_node] = 0


# N : 교차로 개수, M : 골목 개수, A : 시작 교차로, B : 도착 교차로, C : 가진 돈
N, M, A, B, C = map(int, input().split())

# 인접 비용 행렬 ([이동 비용의 합, 골목 요금의 최댓값])
adj = [[1001 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    n, m, c = map(int, input().split())
    adj[n-1][m-1] = adj[m-1][n-1] = c

# 방문 배열
visited = [0 for _ in range(N)]

# 최대 골목 요금의 최솟값
result = 1001

DFS(A-1, B-1, visited, 0, 0)

if result != 1001:
    print(result)
else:
    print(-1)