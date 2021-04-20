# now : 현재 버스의 위치 인덱스, count : 충전 횟수
def e_bus(now, count):

    global min_charge

    # 종점에 도착한 경우
    if now >= N-1:
        if count < min_charge:
            min_charge = count
        return

    # 배터리 교체
    charge = battery[now]
    count += 1

    # 이미 최소 충전 횟수를 넘어선 경우
    if count >= min_charge:
        return
    
    # 갈 수 있는 최대 거리부터 1칸씩 적게 감
    for i in range(charge, 0, -1):
        e_bus(now+i, count)

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    data = list(map(int,input().split()))
    # N : 정류장의 갯수, battery : 정류장별 배터리 용량
    N = data[0]
    battery = data[1:]

    # 최소 충전 횟수
    min_charge = N

    e_bus(0, -1)

    # 출력
    print('#{} {}'.format(test_case, min_charge))