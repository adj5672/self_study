# 단조증가 확인 함수
def st_inc(n):
    N = str(n)
    if len(N) == 1:
        return True
    else:
        for i in range(len(N)-1):
            if N[i] > N[i+1]:
                return False
        else:
            return True

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    As = list(map(int,input().split()))
    max_value = -1

    # Ai * Aj
    for i in range(len(As)-1):
        for j in range(i+1,N):
            # 단조증가 확인 및 최댓값 확인
            if As[i] * As[j] >= max_value and st_inc(As[i] * As[j]):
                max_value = As[i] * As[j]
                
    # 출력
    print('#{} {}'.format(test_case, max_value))