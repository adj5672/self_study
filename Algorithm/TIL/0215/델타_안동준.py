# 2 7 4 3 6
# 8 5 8 3 2
# 2 2 3 6 9
# 5 9 2 5 7
# 3 6 2 9 4

# N * N 행렬
N = 5
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 2차원 배열 생성
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
result = [[0 for _ in range(N)] for _ in range(N)]

# 행렬의 (x, y) 원소마다
for x in range(N):
    for y in range(N):
        # sum : 차이값들의 합
        sum = 0
        for i in range(4):
            # 새로운 좌표 (nx, ny)
            nx, ny = x + dr[i], y + dc[i]
            # 인덱스 범위를 벗어나면 continue
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            else:
                # 절댓값 구하고 sum에 더하기
                sum = sum + (arr[nx][ny] - arr[x][y]) if arr[nx][ny] >= arr[x][y] else sum + (arr[x][y] - arr[nx][ny])
        # 각 (x, y) 에서의 결과값들을 result에 저장하기
        result[x][y] += sum

# 출력
print(result)