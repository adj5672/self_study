# 재귀를 이용한 DFS 함수
def graph(n):
    visit[n] = 1
    for j in range(1,V+1):
        if arr[n][j] == 1 and visit[j] == 0:
            graph(j)

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):

    # V : 노드 갯수, E : 간선 갯수
    V, E = map(int,input().split())
    visit = [0 for _ in range(V+1)]
    result = 0

    # 인접행렬 만들기
    arr = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        n1, n2 = map(int,input().split())
        arr[n1][n2] = 1

    # 시작노드, 도착노드
    S, G = map(int,input().split())

    # 방문 확인
    graph(S)

    # 도착노드 확인
    if visit[G]:
        result = 1

    # 출력
    print('#{} {}'.format(test_case,result))