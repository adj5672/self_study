# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    N, M = map(int,input().split())
    numbers = list(map(int,input().split()))
    # 구간합 최댓값 초기값 설정
    max_value = 0
    for i in range(N-M+1):
        sum_value = 0
        # 이웃한 M개의 합 계산
        for j in range(M):
            sum_value += numbers[i+j]
        # max_value 보다 크면 그 값을 최댓값으로 저장
        if max_value < sum_value:
            max_value = sum_value
    # 구간합 최솟값 초기값 설정
    min_value = max_value
    for i in range(N-M+1):
        sum_value = 0
        # 이웃한 M개의 합 계산
        for j in range(M):
            sum_value += numbers[i+j]
        # min_value 보다 작으면 그 값을 최솟값으로 저장
        if min_value > sum_value:
            min_value = sum_value
    # 출력
    print('#{} {}'.format(test_case,max_value - min_value))