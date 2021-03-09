# test_case 갯수
T = int(input())

for test_case in range(1,T+1):

    # 버스 갯수
    N = int(input())

    # 각 버스 노선 2차원 배열로 정리
    buses = []
    for _ in range(N):
        buses.append(list(map(int,input().split())))

    # 확인할 각 버스 정류장 list로 정리
    P = int(input())
    C = []
    for _ in range(P):
        C.append(int(input()))
    
    # 각 Cj 번 정류장을 지나는 버스의 갯수를 세기 위한 count list 생성
    count = [0] * P

    # Cj번 버스 정류장마다
    for idx, Cj in enumerate(C):
        # 각 버스의 노선이 그 stop 버스 정류장을 지나면 count의 같은 index에 +1을 한다.
        for bus in buses:
            if bus[0] <= Cj <= bus[1]:
                count[idx] += 1
    
    # 출력
    print('#{} {}'.format(test_case,' '.join(map(str,count))))