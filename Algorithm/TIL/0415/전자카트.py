# DFS
def DFS(now, total):

    global min_power
    
    # 방문 체크
    visited[now] = 1

    # 이미 최소 배터리 사용량을 넘어섰다면 return
    if total >= min_power:
        return

    # 모든 관리 구역을 다 돌았을 경우
    if all(visited):
        total += arr[now][0]
        if min_power > total:
            min_power = total
        return

    for i in range(N):
        if visited[i] == 0:
            total += arr[now][i]
            DFS(i, total)
            total -= arr[now][i]
            visited[i] = 0

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # N : 구역의 크기
    N = int(input())

    # arr : 관리구역 정보
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 방문 배열
    visited = [0 for _ in range(N)]

    # min_power : 최소 배터리 소비량
    min_power = 100 * N * N

    DFS(0, 0)

    # 출력
    print('#{} {}'.format(test_case, min_power))