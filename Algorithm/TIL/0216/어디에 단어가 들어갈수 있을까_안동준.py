# test_case 갯수
T = int(input())

for test_case in range(1, T + 1):

    # 단어 퍼즐판 만들기
    N, K = map(int, input().split())
    room, count = [], 0
    for _ in range(N):
        room.append(list(map(int, input().split())))
    
    # 각 열을 2차원 배열로 만들고 각 열의 처음과 끝에 0을 추가
    vert = [[0] for _ in range(N)]
    for hor in room:
        for idx, j in enumerate(hor):
            vert[idx].append(j)
    for v in vert:
        v.append(0)

    # 각 행의 처음과 끝에 0을 추가
    for idx, hor in enumerate(room):
        room[idx] = [0] + hor + [0]

    # 각 행마다 길이가 K인 단어가 들어갈 수 있는 곳 count
    for hor in room:
        for i in range(N - K + 1):
            if hor[i:i + K + 2] == [0] + [1] * K + [0]:
                count += 1

    # 각 열마다 길이가 K인 단어가 들어갈 수 있는 곳 count
    for ver in vert:
        for i in range(N - K + 1):
            if ver[i:i + K + 2] == [0] + [1] * K + [0]:
                count += 1

    print(f'#{test_case} {count}')