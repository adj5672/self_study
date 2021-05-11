def Find_set(x):
    if p[x] == x:
        return x
    else:
        return Find_set(p[x])

def Union(x, y):
    p[Find_set(y)] = Find_set(x)

def Dijkstra(start_index, end_index):

    D = adj[start_index]
    w = start_index

    while True:

        # 방문 처리
        visited[w] = 1
        if all(visited[1:]):
            break

        # 최단 거리 갱신
        for v in range(1, V+1):
            if not visited[v] and adj[w][v] != 1001:
                D[v] = min(D[v], D[w] + adj[w][v])

        # 인접 지역 중 비용이 가장 적은 정점 선택
        new_w = [0, 1001]
        for v in range(1, V+1):
            if not visited[v] and adj[w][v] != 1001:
                if new_w[1] > D[v]:
                    new_w[0], new_w[1] = v, D[v]
        w = new_w[0]

    # start_index 에서 end_index 까지의 최소 비용 return
    return D[end_index]

# test_case 갯수
T = int(input())

for test_case in range(1, T+1):
    # V : 도시의 수, E : 도로의 수, M : 건설 예산
    V, E, M = map(int,input().split())

    # adj : 각 도로 건설 비용을 인접행렬로 표현
    adj = [[1001 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(V+1):
        adj[i][i] = 0
    # data : 도로 정보
    data = []
    for _ in range(E):
        # road : 각 도로에 대한 정보
        road = list(map(int,input().split()))
        adj[road[0]][road[1]] = road[2]
        adj[road[1]][road[0]] = road[2]
        data.append(road)

    # planA : 크루스칼 알고리즘
    planA = 0
    data.sort(key=lambda x: x[2])
    # p : Make_set
    p = [i for i in range(V+1)]
    # 선택된 도로의 갯수가 도시의 갯수 - 1 개 일 때까지
    maked_road = 0
    for road in data:
        c1, c2, cost = road[0], road[1], road[2]
        if Find_set(c1) != Find_set(c2):
            planA += cost
            Union(c1, c2)
            maked_road += 1
        # V-1개의 도로가 선택된 경우
        if maked_road == V-1:
            break

    # planB : 다익스트라 알고리즘
    visited = [0 for _ in range(V+1)]
    planB = Dijkstra(1, V)

    # planA가 가능한 경우
    if planA <= M:
        result = M - planA
    # planB가 가능한 경우
    elif planB <= M:
        result = M - planB
    # 둘 다 불가능한 경우
    else:
        result = -1

    # 출력
    print('#{} {}'.format(test_case, result))