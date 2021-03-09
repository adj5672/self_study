# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    N, M = map(int,input().split())
    max_fly = 0

    # 2차원 배열 만들기
    room = []
    for _ in range(N):
        room.append(list(map(int,input().split())))

    # 파리 잡기
    # (x, y) : 파리채 왼쪽 상단 모서리 좌표
    for x in range(N-M+1):
        for y in range(N-M+1):
            fly = 0
            # 각 (x, y)를 기준으로 파리채로 파리잡기
            for i in range(x,x+M):
                for j in range(y,y+M):
                    fly += room[i][j]
            # 최댓값과 비교
            if fly > max_fly:
                max_fly = fly
                
    # 출력
    print('#{} {}'.format(test_case,max_fly))