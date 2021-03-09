# 색종이의 수
N = int(input())

# 색종이 위치 data
papers = []
for _ in range(N):
    papers.append(list(map(int,input().split())))

# 흰 도화지 준비
arr = [[0 for _ in range(102)] for _ in range(102)]

for paper in papers:
    # (x, y) 색종이 좌측 상단 모서리의 좌표
    x, y = 91 - paper[1], 1 + paper[0]

    # 흰 도화지에 색종이 영역 색칠
    for i in range(10):
        for j in range(10):
            arr[x+i][y+j] = 1

# 델타
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
count = 0

# 모서리 확인하기
# 각 좌표마다
for x in range(102):
    for y in range(102):
        # 색칠 되어 있으면
        if arr[x][y]:
            # 상하좌우 중 0 이 있으면 그 방향 모서리 존재
            for i in range(4):
                if arr[x+dr[i]][y+dc[i]] == 0:
                    count += 1

# 출력
print(count)
