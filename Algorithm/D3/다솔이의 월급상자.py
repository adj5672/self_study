# test_case
T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    average = 0
    
    # 평균 구하기
    for _ in range(N):
        p, x = map(float,input().split())
        average += p * x

    # 출력
    print('#{} {}'.format(test_case, round(average, 6)))