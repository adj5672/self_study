# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    P, Q, R, S, W = map(int,input().split())

    # A사를 이용할 경우 내야되는 수도 요금
    A_charge = P * W

    # B사를 이용할 경우 내야되는 수도 요금
    B_charge = 0
    if W <= R:
        B_charge = Q
    else:
        B_charge = Q + (W - R) * S

    # 출력
    print('#{} {}'.format(test_case, min([A_charge, B_charge])))