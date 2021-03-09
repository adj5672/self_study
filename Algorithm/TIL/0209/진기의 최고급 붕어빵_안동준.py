# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    N, M, K = map(int,input().split())
    people = list(map(int,input().split()))
    # people list 오름차순 정렬
    for _ in range(N-1):
        for i in range(N-1):
            if people[i] > people[i+1]:
                people[i], people[i+1] = people[i+1], people[i]
    # 기본 결과값 설정(Possible)
    result = 'Possible'
    for idx, person in enumerate(people):
        # idx번째 손님이 왔을 때 남아있는 붕어빵의 갯수
        boong = (person // M) * K - idx
        # 만약 남아있는 붕어빵이 없다면 결과값 Impossible 반환
        if boong <= 0:
            result = 'Impossible'
            break
    # 출력
    print('#{} {}'.format(test_case,result))
