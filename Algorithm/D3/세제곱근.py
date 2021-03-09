T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    m = int(N ** 0.34)
    if N == 1:
        result = 1
    else:
        for i in range(2, m+1):
            if i ** 3 == N:
                result = i
                break
        else:
            result = -1

    print('#{} {}'.format(test_case, result))  