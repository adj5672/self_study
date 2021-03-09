# test_Case 갯수
T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    rotation = [[0 for _ in range(N)] for _ in range(N)]
    result = []

    # 숫자 받아오기
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    
    # 90도, 180도, 270도 회전
    for _ in range(3):
        # 90도 회전
        for x in range(N):
            for y in range(N):
                rotation[y][(N-1)-x] = arr[x][y]
        # result에 append
        result.append(rotation)
        # arr를 90도 회전 후로 변환
        for x in range(N):
            for y in range(N):
                arr[x][y] = rotation[x][y]
        # rotation 초기화
        rotation = [[0 for _ in range(N)] for _ in range(N)]

    # 출력
    print('#{}'.format(test_case))
    for row in range(N):
        r_result = []
        for mat in result:
            r_result.append(''.join(map(str,mat[row])))
        print(' '.join(r_result))