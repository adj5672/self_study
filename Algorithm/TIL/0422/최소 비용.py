# extra : 높이차로 발생하는 추가 연료량
def BFS(x, y, extra):
    pass

# test_case 갯수
T = int(input())

for test_case in range(1, T + 1):
    # N : 가로 세로 칸 수
    N = int(input())

    # 각 지역의 높이
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 해당 지역까지 가는데 드는 최소 소비 연료량
    key = [[2000 for _ in range(N)] for _ in range(N)]
