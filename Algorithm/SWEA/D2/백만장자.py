# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    # 가격 정보
    price = list(map(int,input().split()))
    # 수익
    revenue = 0

    while price:
        # 최댓값 찾기
        max_price = max(price)
        
        # 각 가격마다
        for idx, num in enumerate(price):
            # 최댓값이 아니면 그 날 구입으로 수익에서 가격을 빼고
            if num != max_price:
                revenue -= num
            # 최댓값인 날이라면 사놓은 물건을 모두 판다.
            else:
                revenue += idx * num
                # 그 날 이후부터 다시 진행한다.
                price = price[idx+1:]
                break

    # 출력
    print('#{} {}'.format(test_case, revenue))