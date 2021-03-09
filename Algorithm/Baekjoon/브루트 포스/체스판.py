# 좌표가 체스판의 좌측 상단점일때 체스판을 만들기 위해 색칠해야 하는 칸의 최솟값
def color(x,y):

    count_w, count_b = 0, 0

    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if chess[x+i][y+j] != 'W':
                    count_w += 1
            else:
                if chess[x+i][y+j] != 'B':
                    count_w += 1

    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if chess[x+i][y+j] != 'B':
                    count_b += 1
            else:
                if chess[x+i][y+j] != 'W':
                    count_b += 1

    return min([count_w, count_b])


# N * M 체스판
N, M = map(int,input().split())

# 체스판
chess = [list(input()) for _ in range(N)]

min_count = N * M

for x in range(N - 7):
    for y in range(M - 7):
        sub_min = color(x,y)
        if min_count > sub_min:
            min_count = sub_min

# 출력
print(min_count)
        