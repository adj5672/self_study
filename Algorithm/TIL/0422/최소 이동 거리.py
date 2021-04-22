def Dijkstra(start_node, end_node):

    D = [x for x in adj[start_node]]
    w = start_node

    while True:

        # 방문처리
        visited[w] = 1
        if all(visited):
            break

        # 방문하지 않았고 인접했을 경우 key 값 갱신
        for v in range(N+1):
            if not visited[v] and adj[w][v] != 1000001:
                D[v] = min(D[v], D[w] + adj[w][v])

        # 선택 되지 않은 정점 중 key 값이 가장 적은 정점 선택
        new_w = [0, 1000002]
        for j in range(N+1):
            if not visited[j] and new_w[1] > D[j]:
                new_w[0], new_w[1] = j, D[j]
        w = new_w[0]

    # 도착 지점의 key값 return
    return D[end_node]

# test_case 갯수
T = int(input())

for test_case in range(1, T+1):
    # N : 마지막 연결지점 번호, E : 도로의 갯수
    N, E = map(int,input().split())

    # 인접 행렬 (가중치 적용)
    adj = [[1000001 for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(E):
        u, v, w = map(int,input().split())
        adj[u][v] = w
    
    # 방문배열 및 결과값
    visited = [0 for _ in range(N+1)]
    result = Dijkstra(0, N)
    
    # 출력
    print('#{} {}'.format(test_case, result))
