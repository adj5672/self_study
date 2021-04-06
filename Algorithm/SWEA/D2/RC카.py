# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # command 갯수
    N = int(input())

    # command 받아오기
    command = []
    for _ in range(N):
        command.append(list(map(int,input().split())))

    velocity, distance = 0, 0
    for c in command:
        # command 가 0 이면
        if c[0] == 0:
            # 현재 속도만큼 거리이동
            distance += velocity
        # command 가 1이면
        elif c[0] == 1:
            # 속도를 올리고 이후 속도만큼 거리 이동
            velocity += c[1]
            distance += velocity
        # command 가 2이면
        else:
            velocity = max([0, velocity - c[1]])
            distance += velocity
            
    # 출력
    print('#{} {}'.format(test_case, distance))