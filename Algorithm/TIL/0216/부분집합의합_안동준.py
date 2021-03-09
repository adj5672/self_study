# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split())
    arr = list(range(1,13))
    n, count = len(arr), 0

    # 부분집합 만들기
    for i in range(1 << n):
        subset, sum_subset = [], 0
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        # 부분집합 원소의 합 구하기
        for num in subset:
            sum_subset += num
        # 조건을 만족하는지 확인하기
        if sum_subset == K and len(subset) == N:
            count += 1

    # 결과 출력
    print('#{} {}'.format(test_case,count))