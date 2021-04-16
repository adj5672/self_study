# DFS (stack을 이용)
def DFS(x, y):

    stack = [[x, y]]
    # 이동 횟수
    move = 1

    while stack:
        # 현재 좌표 정보
        cur = stack.pop()
        cur_x, cur_y = cur[0], cur[1]
        # 사방 탐색
        for i in range(4):
            nx, ny = cur_x + dr[i], cur_y + dc[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 현재 숫자보다 정확히 1 큰 경우
                if arr[nx][ny] == arr[cur_x][cur_y] + 1:
                    # 이동할 위치의 이동 횟수 정보를 알고 있을 경우
                    if count[arr[nx][ny]]:
                        move += count[arr[nx][ny]]
                        count[arr[x][y]] = move
                        return
                    # 이동할 위치의 이동 횟수 정보를 모르는 경우
                    else:
                        stack.append([nx, ny])
                        move += 1

    # 가능할 떄 까지 이동 후 시작점의 이동 횟수 정보 저장
    count[arr[x][y]] = move

# test_case 갯수
T = int(input())

# 델타 (상 하 좌 우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for test_case in range(1,T+1):
    # N : 방의 크기
    N = int(input())

    # 방의 정보
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 방문 배열
    count = [0] * (N ** 2 + 1)

    # 각 좌표에서 DFS
    for i in range(N):
        for j in range(N):
            DFS(i, j)

    # 최댓값 찾기
    result = max(count)

    # 출력
    print('#{} {} {}'.format(test_case, count.index(result), result))