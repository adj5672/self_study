# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # N : 신청서 갯수
    N = int(input())

    # data : 도킹 신청서
    data = [list(map(int,input().split())) for _ in range(N)]

    # result : 최종적으로 도킹할 화물들
    result = []

    # available_time : 도킹 시작 가능 시각 = 마지막 도킹이 끝난 시각
    available_time = 0

    while data:

        # 도킹 불가능한 화물들 전부 제거
        for _ in range(len(data)):
            for idx, time in enumerate(data):
                if time[0] < available_time:
                    data.pop(idx)
                    break
            else:
                break

        if data:
            # 도킹 가능 화물 중 종료시간이 가장 빠른 화물 찾기
            dock = 0
            for idx, time in enumerate(data):
                if time[1] < data[dock][1]:
                    dock = idx
            # docking : 도킹할 화물
            docking = data.pop(dock)
            result.append(docking)
            # 도킹 가능 시각 변경
            available_time = docking[1]

    # 출력
    print('#{} {}'.format(test_case, len(result)))
