# DFS
def DFS(x, y, total):

    global min_total

    # 이미 최소합을 넘어선 경우 return
    if total >= min_total:
        return
    
    # 도착지점에 도착했을 경우 최소합과 비교 및 갱신
    if x == N-1 and y == N-1:
        total += arr[x][y]
        if total < min_total:
            min_total = total
        return

    # 아래로 이동
    if x + 1 < N:
        total += arr[x][y]
        DFS(x+1, y, total)
        total -= arr[x][y]
    # 우측으로 이동
    if y + 1 < N:
        total += arr[x][y]
        DFS(x, y + 1, total)
        total -= arr[x][y]


# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # N : 가로, 세로 칸 수
    N = int(input())

    # arr : 숫자가 적힌 판
    arr = [list(map(int,input().split())) for _ in range(N)]

    # min_total : 최소합
    min_total = 10 * N * N

    DFS(0, 0, 0)

    # 출력
    print('#{} {}'.format(test_case, min_total))

