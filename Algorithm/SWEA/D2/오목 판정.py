# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    result = 0

    # 바둑판 만들기
    arr = []
    for _ in range(N):
        arr.append(list(input()))

    # 시작점 (x, y) 기준
    for x in range(N):
        if result:
            break
        for y in range(N):
            if result:
                break
            # 만약 (x, y)에 바둑돌이 있으면
            if arr[x][y] == 'o':
                # 가로 확인 조건
                if y <= N - 5:
                    # 우측 대각선 확인 조건 및 확인
                    if x <= N - 5:
                        for i in range(5):
                            if arr[x+i][y+i] == '.':
                                break
                        else:
                            result = 1
                    # 가로 확인
                    for i in range(5):
                        if arr[x][y+i] == '.':
                            break
                    else:
                        result = 1
                # 세로 방향 확인 조건
                if x <= N - 5:
                    # 좌측 대각선 확인 조건 및 확인
                    if y >= 4:
                        for i in range(5):
                            if arr[x+i][y-i] == '.':
                                break
                        else:
                            result = 1
                    # 세로 확인
                    for i in range(5):
                        if arr[x+i][y] == '.':
                            break
                    else:
                        result = 1
                        
    # 출력
    if result:
        print('#{} YES'.format(test_case))
    else:
        print('#{} NO'.format(test_case))