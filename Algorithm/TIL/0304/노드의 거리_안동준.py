# BFS
def BFS(v):
    # 출발 노드 append
    queue.append(v)
    
    while queue:
        # cur : 현재 노드
        cur = queue.pop(0)
        for i in range(1,V+1):
            # 현재 노드에서 방문하지 않은 인접 노드는
            if adj[cur][i] == 1 and visited[i] == 0:
                # queue에 append 하고 현재 노드의 거리 값 + 1 인 값을 방문 배열에 저장
                queue.append(i)
                visited[i] = visited[cur] + 1

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # V : 노드의 갯수, E : 간선의 갯수
    V, E = map(int,input().split())
    queue = []

    # 인접행렬 만들기
    adj = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        n1, n2 = map(int,input().split())
        adj[n1][n2] = adj[n2][n1] = 1

    # 출발 노드와 도착 노드
    S, G = map(int,input().split())

    # 방문 배열 (방문 배열에 거리 값을 저장한다.)
    visited = [0 for _ in range(V+1)]

    # BFS 함수 실행 및 출발점 거리 초기화
    BFS(S)
    visited[S] = 0
    
    # 출발 노드와 도착 노드 사이의 거리
    result = visited[G]

    # 출력
    print('#{} {}'.format(test_case, result))