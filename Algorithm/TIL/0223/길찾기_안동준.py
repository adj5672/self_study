# DFS
def DFS(n):
    visit[n] = 1
    for j in range(100):
        if arr[n][j] == 1 and visit[j] == 0:
            DFS(j)

for _ in range(10):
    # test_case 번호와 간선의 갯수
    test_case, E = map(int,input().split())

    # 간선 정보 및 방문기록
    edge = list(map(int,input().split()))
    visit = [0 for _ in range(100)]
    
    # 인접행렬 만들기
    arr = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(E):
        n1, n2 = edge[2 * i], edge[2 * i + 1]
        arr[n1][n2] = 1

    # DFS 재귀함수 실행
    DFS(0)

    # 출력
    print('#{} {}'.format(test_case, visit[99]))