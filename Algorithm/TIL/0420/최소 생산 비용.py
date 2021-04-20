# idx : 제품 번호, cost : 비용
def DFS(idx, cost):

    global min_cost
    
    # 공장과 제품을 모두 선택했을 경우
    if idx == N:
        if cost < min_cost:
            min_cost = cost
        return

    # 이미 최소비용을 넘어선 경우 return
    if cost > min_cost:
        return
    
    # 각 공장마다
    for i in range(N):
        # 공장에서 제품 생산이 안되었다면
        if not visited[i]:
            visited[i] = 1
            DFS(idx+1, cost + arr[idx][i])
            visited[i] = 0

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # N : 제품의 수
    N = int(input())
    # 공장별 생산비용
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 방문 배열 (공장)
    visited = [0] * N

    # 최소 비용
    min_cost = 100 * N

    DFS(0, 0)

    # 출력
    print('#{} {}'.format(test_case, min_cost))