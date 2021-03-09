# SWEA 1954. 달팽이 숫자

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # N * N 2차원 배열
    N = int(input())
    room =[[0 for _ in range(N)] for _ in range(N)]
    
    # x행 y열
    x, y, num = 0, 0, 2
    room[0][0] = 1

    # N이 1이 아닐 때
    if N != 1:
        while num <= N ** 2:
            
            # 인덱스를 넘어가기 전이나 숫자가 채워진 공간전까지 오른쪽으로 숫자들을 순서대로 채워넣는다.
            while num <= N ** 2:
                room[x][y+1] = num
                y += 1
                num += 1
                if y + 1 >= N or room[x][y+1]:
                    break
                
            # 인덱스를 넘어가기 전이나 숫자가 채워진 공간전까지 아래쪽으로 숫자들을 순서대로 채워넣는다.
            while num <= N ** 2:
                room[x+1][y] = num
                x += 1
                num += 1
                if x + 1 >= N or room[x+1][y]:
                    break
                    
            # 인덱스를 넘어가기 전이나 숫자가 채워진 공간전까지 왼쪽으로 숫자들을 순서대로 채워넣는다.
            while num <= N ** 2:
                room[x][y-1] = num
                y -= 1
                num += 1
                if y - 1 < 0 or room[x][y-1]:
                    break

            # 인덱스를 넘어가기 전이나 숫자가 채워진 공간전까지 위쪽으로 숫자들을 순서대로 채워넣는다.
            while num <= N ** 2:
                room[x-1][y] = num
                x -= 1
                num += 1
                if x - 1 < 0 or room[x-1][y]:
                    break
                    
    # 출력
    print('#{}'.format(test_case))
    for row in room:
        print(' '.join(map(str,row)))