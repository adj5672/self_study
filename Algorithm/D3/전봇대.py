# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # 전선의 갯수
    N = int(input())

    # 전선의 위치 정보
    line = []
    for _ in range(N):
        line.append(list(map(int,input().split())))

    # 교차점 count
    count = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if (line[i][0] - line[j][0]) * (line[i][1] - line[j][1]) < 0:
                count += 1

    # 출력
    print('#{} {}'.format(test_case, count))
