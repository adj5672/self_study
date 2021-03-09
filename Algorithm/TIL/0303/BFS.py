# 간선 정보
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

# BFS
def BFS(x):

    # 출발 정점을 queue에 append하고 방문 처리
    queue.append(x)
    visited[x] = 1

    while queue:
        # 현재 위치 pop 하고 print
        cur = queue.pop(0)
        print(cur,end=' ')
        # cur의 인접한 정점들에 대해 queue에 append하고 방문 처리
        for i in range(n+1):
            if adj[cur][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1

# node 갯수
n = 7
# 간선 정보
edge = list(map(int,input().split()))
# 인접행렬 만들기
adj = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(len(edge)//2):
    adj[edge[2 * i]][edge[2 * i + 1]] = 1
    adj[edge[2 * i + 1]][edge[2 * i]] = 1
# 방문배열
visited = [0 for _ in range(n+1)]
queue = []

# BFS 함수 실행
BFS(1)