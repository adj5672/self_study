# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    N, M = map(int,input().split())
    result = 'ON'
    # 비트 마스크
    for j in range(N):
        if not M & (1 << j):
            result = 'OFF'
            break
    # 출력
    print('#{} {}'.format(test_case, result))
