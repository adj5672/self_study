# T = test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # N = 주어지는 양수의 갯수
    N = int(input())
    # 주어진 양수들을 list로 변환
    numbers = list(map(int,input().split()))
    max, min = numbers[0], numbers[0]
    # numbers에 저장된 각 num마다
    for num in numbers:
        # max값 보다 크면 그 값을 max 변수에 저장
        if num > max:
            max = num
        # min값 보다 작으면 그 값을 min 변수에 저장
        elif num < min:
            min = num
    # 최댓값 최솟값 차이 출력
    print('#{} {}'.format(test_case,max-min))


