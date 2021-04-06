# test_case 갯수
T = int(input())

for test_case in range(1,T+1):

    # N : 총 사람 수, A : P채널 구독자 수, B : Q채널 구독자 수
    N, A, B = map(int,input().split())

    # 최대, 최소 구독자 수
    max_sub, min_sub = 0, 0

    # 최대 구독자 수
    max_sub = min([A, B])

    # 최소 구독자 수
    if A + B <= N:
        min_sub = 0
    else:
        min_sub = (A + B) - N

    # 출력
    print('#{} {} {}'.format(test_case, max_sub, min_sub))