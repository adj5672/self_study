# test_case 갯수
T = int(input())

for test_case in range(1,T+1):

    N = int(input())
    numbers = list(map(int,input().split()))

    # numbers 의 각 index에 대해서
    for idx in range(N):

        # index가 짝수면 큰 수 선택정렬
        if idx % 2 == 0:
            max_index = idx
            for i in range(idx, N):
                if numbers[i] >= numbers[max_index]:
                    max_index = i
            numbers[idx], numbers[max_index] = numbers[max_index], numbers[idx]

        # index가 홀수면 작은 수 선택정렬
        else:
            min_index = idx
            for i in range(idx, N):
                if numbers[i] <= numbers[min_index]:
                    min_index = i
            numbers[idx], numbers[min_index] = numbers[min_index], numbers[idx]

    # 출력
    print('#{} {}'.format(test_case,' '.join(map(str,numbers[:10]))))