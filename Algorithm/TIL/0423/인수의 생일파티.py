def Dijkstra(start_node, matrix):

    D = [x for x in matrix[start_node]]
    w = start_node

    while True:

        # 방문처리
        visited[w] = 1
        if all(visited):
            break

        # 방문하지 않았고 인접했을 경우 key 값 갱신
        for v in range(N):
            if visited[v] == 0 and matrix[w][v] != 1000001:
                D[v] = min(D[v], D[w] + matrix[w][v])

        # 선택 되지 않은 정점 중 key 값이 가장 적은 정점 선택
        new_w = [0, 1000002]
        for j in range(N):
            if visited[j] == 0 and new_w[1] > D[j]:
                new_w[0], new_w[1] = j, D[j]
        w = new_w[0]

    return D

# test_case 갯수
T = int(input())

for test_case in range(1, T + 1):
    # N : 집의 갯수, M : 도로의 갯수, X : 인수의 집 번호
    N, M, X = map(int, input().split())

    # 인접 행렬
    adj = [[1000001 for _ in range(N)] for _ in range(N)]
    adj_t = [[1000001 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        adj[i][i] = 0
        adj_t[i][i] = 0
    for _ in range(M):
        x, y, c = map(int, input().split())
        adj[x - 1][y - 1] = c
        adj_t[y - 1][x - 1] = c

    # D1 : 인수 집에서 다른 집으로 가는 최소 거리
    # D2 : 다른 집에서 인수 집으로 가는 최소 거리
    visited = [0] * N
    D1 = Dijkstra(X-1, adj)
    visited = [0] * N
    D2 = Dijkstra(X-1, adj_t)
    
    # 최대값 갱신
    max_length = 0
    for i in range(N):
        if D1[i] + D2[i] > max_length:
            max_length = D1[i] + D2[i]

    # 출력
    print('#{} {}'.format(test_case, max_length))