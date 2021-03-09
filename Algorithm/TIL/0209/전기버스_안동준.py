# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    K, N, M = map(int,input().split())
    # 충전기가 있는 정류장 번호
    charge_station = list(map(int,input().split()))
    # station : 정류장, 충전기가 있는 곳은 1, 없는 곳은 0
    station = [0] * (N+K+1)
    for i in charge_station:
        station[i] = 1
    # charge : 충전 횟수, bus : 버스의 현재 위치
    charge, bus = 0, 0
    while True:
        # 만약 bus가 종점을 지나면 while문 종료
        if bus + K >= N:
            break
        # 현재 버스위치 + K 정류장(최대한 갈 수 있는 정류장)서부터 
        # 한 정류장씩 가까워지며 충전기가 있는 정류장 확인
        for i in range(bus+K, bus, -1):
            # 만약 충전기가 있다면 충전횟수 + 1, 충전기가 있는 정류장에 버스 위치하고 for문 종료
            if station[i] == 1:
                bus = i
                charge += 1
                break
        # 만약 for문에서 충전기가 있는 정류장을 발견 못했다면
        # 결과값 charge를 0으로 바꾸고 while문 종료
        else:
            charge = 0
            break
    # 출력        
    print('#{} {}'.format(test_case,charge))