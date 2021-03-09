# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # N : 상자의 갯수, Q : 변경 횟수
    N, Q = map(int,input().split())
    # Box : 번호가 적힌 박스
    Box = [0 for _ in range(N)]

    # 각 i 번째 작업마다 L, R을 받아온다.
    for i in range(1,Q+1):
        L, R = map(int,input().split())
        # L 번째 상자부터, R 번째 상자까지 작업을 수행한다.
        for j in range(L-1,R):
            Box[j] = i
            
    # 출력
    print('#{} {}'.format(test_case, ' '.join(map(str,Box))))