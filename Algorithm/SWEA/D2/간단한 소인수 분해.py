# test_case 갯수
T = int(input())
# 소인수
prime = [2, 3, 5, 7, 11]

for test_case in range(1,T+1):

    # 정수 N, 각 소인수 count 배열, index번호 i
    N = int(input())
    count = [0 for _ in range(5)]
    i = 0

    # prime index를 벗어날 때까지
    while i < 5:
        
        # 각 소인수로 안나누어 떨어질 때까지 나누면서 count
        while True:
            if N % prime[i] == 0:
                count[i] += 1
                N = N / prime[i]
            else:
                break

        # 다음 소인수로    
        i += 1
    
    # 출력
    print('#{} {}'.format(test_case,' '.join(map(str,count))))