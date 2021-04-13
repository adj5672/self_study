# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # N : 비트 갯수, M : 숫자
    N, M = map(int,input().split())

    # 기본 결과값 ON
    result = 'ON'
    # 비트 연산을 통해
    for i in range(N):
        # M의 이진수 표현 중 뒤에서부터 0이 하나라도 나올경우
        if not M & (1 << i):
            # result = 'OFF'
            result = 'OFF'
            break

    # 출력
    print('#{} {}'.format(test_case, result))
