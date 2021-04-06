# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    # 본 숫자를 확인
    count = [0 for _ in range(10)]
    i = 1

    while True:
        # 확인할 정수
        xN = N * i
        # 각 자릿수 확인
        for num in str(xN):
            if count[int(num)] == 0:
                count[int(num)] = 1
        # 만약 모든 숫자가 count 되었다면 break
        if all(count):
            break
        # 아니라면 다음 숫자를 센다
        i += 1

    # 출력
    print('#{} {}'.format(test_case, xN))
