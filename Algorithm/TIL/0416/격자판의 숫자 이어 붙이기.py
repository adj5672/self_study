def DFS(x, y, c, num):

    # 7자리 숫자가 완성되었다면 결과에 추가
    if c == 7:
        result.add(num)
        return
    
    # 각 방향으로 이동
    for i in range(4):
        if 0 <= x + dr[i] < 4 and 0 <= y + dc[i] < 4:
            DFS(x + dr[i], y + dc[i], c+1, num + arr[x + dr[i]][y + dc[i]])

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):

    # 격자판 정보
    arr = [input().split() for _ in range(4)]

    # result : 가능한 7자리 숫자
    result = set()

    # 델타 (상 하 좌 우)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 격자판의 각 좌표를 시작점으로 DFS
    for i in range(4):
        for j in range(4):
            DFS(i, j, 1, arr[i][j])

    # 출력
    print('#{} {}'.format(test_case, len(result)))