# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # N : 손님 수, M : K개를 만드는 데 걸리는 시간, K : M초마다 만드는 붕어빵 갯수
    N, M, K = map(int,input().split())
    # sale : 손님들이 오는 시간
    time = list(map(int,input().split()))
    # time 정렬 (버블 정렬)
    for i in range(N):
        for j in range(N-1):
            if time[j] > time[j+1]:
                time[j], time[j+1] = time[j+1], time[j]

    result = 'Possible'
    # 각 손님마다 붕어빵이 남아있는지 확인
    for idx, p in enumerate(time):
        # bread : 남아있는 붕어빵의 갯수
        # (p // M) * K : p초 일때까지 만들 수 있는 붕어빵의 갯수
        # idx : 팔린 붕어빵의 갯수
        bread = (p // M) * K - idx
        # 남아있는 붕어빵이 없다면
        if bread <= 0:
            # 불가능
            result = 'Impossible'
            break

    # 출력
    print('#{} {}'.format(test_case, result))
