'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과(재귀)를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

입력1
4 5 1
1 2
1 3
1 4
2 4
3 4

출력1
1 2 4 3
1 2 3 4

입력2
5 5 3
5 4
5 2
1 2
3 4
3 1

출력2
3 1 2 5 4
3 1 4 2 5

입력1
1000 1 1000
999 1000

출력2
1000 999
1000 999
'''

# DFS
def DFS(x):
    visited_dfs[x] = 1
    result_dfs.append(x)

    for i in range(1,N+1):
        if arr[x][i] == 1 and visited_dfs[i] == 0:
            DFS(i)

# BFS
def BFS(x):

    queue.append(x)
    visited_bfs[x] = 1

    while queue:
        cur = queue.pop(0)
        result_bfs.append(cur)
        for i in range(1,N+1):
            if arr[cur][i] == 1 and visited_bfs[i] == 0:
                queue.append(i)
                visited_bfs[i] = 1

for tc in range(1,4):
    # N : 정점 갯수, M : 간선 갯수, V : 시작 정점 번호
    N, M, V = map(int,input().split())
    queue = []
    
    # 인접행렬 만들기
    arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        n1, n2 = map(int,input().split())
        arr[n1][n2] = 1
        arr[n2][n1] = 1
    
    # 방문 배열
    visited_dfs = [0 for _ in range(N+1)]
    visited_bfs = [0 for _ in range(N+1)]
    
    # 방문순서
    result_dfs = []
    result_bfs = []
    
    # 함수 실행
    DFS(V)
    BFS(V)

    # 출력
    print(' '.join(map(str,result_dfs)))
    print(' '.join(map(str,result_bfs)))