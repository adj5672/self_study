def N_Queen(idx):

    global count

    # N개의 퀸을 다 놓은 경우
    if idx == N:
        count += 1
        return

    # idx 번째 행에 퀸을 놓을 수 없는 경우
    if all(chess[idx]):
        return

    # idx 행, i 열에 퀸을 놓는다.
    for i in range(N):
        if not chess[idx][i]:

            # idx 행 이상, i 열 모두 방문처리
            for row in range(idx, N):
                chess[row][i] += 1
            # 좌, 우측 대각선 아랫방향 방문처리
            for j in range(N-idx):
                if i - j >= 0:
                    chess[idx+j][i-j] += 1
                if i + j < N:
                    chess[idx+j][i+j] += 1

            N_Queen(idx+1)

            # idx 행 이상, i 열 모두 방문처리 취소
            for row in range(idx, N):
                chess[row][i] -= 1
            # 좌, 우측 대각선 아랫방향 방문처리 취소
            for j in range(N - idx):
                if i - j >= 0:
                    chess[idx+j][i-j] -= 1
                if i + j < N:
                    chess[idx+j][i+j] -= 1

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # N : 보드의 크기
    N = int(input())
    
    # 체스판
    chess = [[0 for _ in range(N)] for _ in range(N)]

    # 경우의 수
    count = 0

    N_Queen(0)

    # 출력
    print('#{} {}'.format(test_case, count))