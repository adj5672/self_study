# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    p, q = map(float,input().split())

    s1 = (1-p) * q
    s2 = p * (1-q) * q

    if s1 < s2:
        result = 'YES'
    else:
        result = 'NO'

    # 출력
    print('#{} {}'.format(test_case, result))