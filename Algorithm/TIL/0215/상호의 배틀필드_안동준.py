T = int(input())

for test_case in range(1,T+1):
    H, W = map(int,input().split())

    # map 만들기
    game_map = [0] * H
    for i in range(H):
        game_map[i] = list(input())

    # 명령의 갯수와 명령
    N = int(input())
    orders = input()

    # tank의 현재 위치 찾기
    tank_x, tank_y = 0, 0
    for x, i in enumerate(game_map):
        for y, j in enumerate(i):
            if j in ['<', '>', '^', 'v']:
                tank_x, tank_y = x, y

    # 각 명령마다
    for order in orders:
        # 발사할 경우
        if order == 'S':
            # 왼쪽 발사
            if game_map[tank_x][tank_y] == '<':
                for i in range(tank_y, -1, -1):
                    if game_map[tank_x][i] == '*':
                        game_map[tank_x][i] = '.'
                        break
                    elif game_map[tank_x][i] == '#':
                        break
            # 오른쪽 발사
            if game_map[tank_x][tank_y] == '>':
                for i in range(tank_y, W):
                    if game_map[tank_x][i] == '*':
                        game_map[tank_x][i] = '.'
                        break
                    elif game_map[tank_x][i] == '#':
                        break
            # 위쪽 발사
            if game_map[tank_x][tank_y] == '^':
                for i in range(tank_x, -1, -1):
                    if game_map[i][tank_y] == '*':
                        game_map[i][tank_y] = '.'
                        break
                    elif game_map[i][tank_y] == '#':
                        break
            # 아래쪽 발사
            if game_map[tank_x][tank_y] == 'v':
                for i in range(tank_x, H):
                    if game_map[i][tank_y] == '*':
                        game_map[i][tank_y] = '.'
                        break
                    elif game_map[i][tank_y] == '#':
                        break
        # 위쪽으로 이동할 경우
        if order == 'U':
            if tank_x - 1 >= 0:
                if game_map[tank_x - 1][tank_y] == '.':
                    game_map[tank_x][tank_y] = '.'
                    game_map[tank_x - 1][tank_y] = '^'
                    tank_x -= 1
                else:
                    game_map[tank_x][tank_y] = '^'
            else:
                game_map[tank_x][tank_y] = '^'
        # 아래쪽으로 이동할 경우
        if order == 'D':
            if tank_x + 1 < H:
                if game_map[tank_x + 1][tank_y] == '.':
                    game_map[tank_x][tank_y] = '.'
                    game_map[tank_x + 1][tank_y] = 'v'
                    tank_x += 1
                else:
                    game_map[tank_x][tank_y] = 'v'
            else:
                game_map[tank_x][tank_y] = 'v'
        # 왼쪽으로 이동할 경우
        if order == 'L':
            if tank_y - 1 >= 0:
                if game_map[tank_x][tank_y - 1] == '.':
                    game_map[tank_x][tank_y] = '.'
                    game_map[tank_x][tank_y - 1] = '<'
                    tank_y -= 1
                else:
                    game_map[tank_x][tank_y] = '<'
            else:
                game_map[tank_x][tank_y] = '<'
        # 오른쪽으로 이동할 경우
        if order == 'R':
            if tank_y + 1 < W:
                if game_map[tank_x][tank_y + 1] == '.':
                    game_map[tank_x][tank_y] = '.'
                    game_map[tank_x][tank_y + 1] = '>'
                    tank_y += 1
                else:
                    game_map[tank_x][tank_y] = '>'
            else:
                game_map[tank_x][tank_y] = '>'

    # 결과값 출력
    print('#{} {}'.format(test_case,''.join(game_map[0])))
    for i in range(1,H):
        print(''.join(game_map[i]))