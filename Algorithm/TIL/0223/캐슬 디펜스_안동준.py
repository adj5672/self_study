# N : 행의 수, M : 열의 수, D : 공격 거리
N, M, D = map(int,input().split())

# 맵 만들기
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
arr.append([0 for _ in range(M)])

# 궁수를 성에 배치하는 경우 모두 구하기
archer = []
for i in range(1 << M):
    subset = [0 for _ in range(M)]
    for j in range(M):
        if i & (1 << j):
            subset[j] = 2
    if sum(subset) == 6:
        archer.append(subset)

max_kill = 0
# 각 궁수 배치마다 죽일 수 있는 적 구하기
for i in range(len(archer)):
    kill = 0
    # 성에 궁수 배치
    arr[-1] = archer[i]

    while True:

        for j in range(M):
            # 성 순회 중 만약 궁수라면
            if arr[N][j] == 2:
                shot = 0
                # 적을 찾아 죽이고 값 계산
                for x in range(N-1,-1,-1):
                    if shot:
                        break
                    for y in range(M):
                        if (N - x) + abs(j - y) <= D and arr[x][y] == 1:
                            arr[x][y] = 0
                            kill += 1
                            shot = 1
                            break

        # 살아남은 적들 한칸씩 이동
        for x in range(N):
            for y in range(M):
                if arr[x][y] == 1:
                    if x == N-1:
                        arr[x][y] = 0
                    else:
                        arr[x][y] = 0
                        arr[x+1][y] = 1

        # 남은 적이 없다면 while문 break
        if

