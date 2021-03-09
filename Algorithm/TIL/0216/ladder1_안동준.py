for _ in range(10):
    # test_case number
    test_case = int(input())

    # 사다리 그리기
    room = []
    for _ in range(100):
        room.append(list(map(int,input().split())))

    # 도착지점 찾기
    x, y = 99, 0
    for i in range(100):
        if room[99][i] == 2:
            y = i
        break

    # 도착지점에서 사다리를 거슬러 올라가는 방법
    # 도착시 x = 0이되고 while문 종료
    while x != 0:

        # 왼쪽이나 오른쪽에 1이 나타날 떄까지 계속 위로 올라감
        while (not room[x][y - 1] or y - 1 < 0) and (not room[x][(y + 1) % 100] or y + 1 > 99):
            x -= 1
            if x == 0:
                break

        # 왼쪽에 1이 있으면 왼쪽으로 끝까지 이동하고 한칸 위로 올라감
        if room[x][y - 1] and y - 1 > 0:
            while room[x][y - 1]:
                y -= 1
                if y == 0:
                    break
            x -= 1

        # 오른쪽에 1이 있으면 오른쪽으로 끝까지 이동하고 한칸 위로 올라감
        elif room[x][(y + 1) % 100] and y + 1 < 100:
            while room[x][y + 1]:
                y += 1
                if y == 99:
                    break
            x -= 1

    # 출력
    print('#{} {}'.format(test_case,y))
