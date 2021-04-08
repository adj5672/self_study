# 벽 세우기
def build_wall(lab, s_x):

    global wall
    global safe_area

    for x in range(s_x, N):
        for y in range(M):
            if lab[x][y] == 0:
                lab[x][y] = 1
                wall += 1
                # 만약 벽이 3개라면
                if wall == 3:
                    # 최대 안전구역과 비교
                    count = virus(lab)
                    if count > safe_area:
                        safe_area = count
                else:
                    build_wall(lab, x)
                lab[x][y] = 0
                wall -= 1
    
# 바이러스가 퍼진다~
def virus(lab):

    v = []
    restore = []
    count = 0

    # 시작 바이러스 위치 확인
    for x in range(N):
        for y in range(M):
            if lab[x][y] == 2:
                v.append([x,y])

    # BFS 사용해서 바이러스 확산시킴
    for v_idx in v:
        queue = []
        queue.append(v_idx)
        while queue:
            cur = queue.pop(0)
            cur_x, cur_y = cur[0], cur[1]
            for i in range(4):
                if 0 <= cur_x + dr[i] < N and 0 <= cur_y + dc[i] < M:
                    if lab[cur_x + dr[i]][cur_y + dc[i]] == 0:
                        queue.append([cur_x + dr[i], cur_y + dc[i]])
                        restore.append([cur_x + dr[i], cur_y + dc[i]])
                        lab[cur_x + dr[i]][cur_y + dc[i]] = 2

    # 안전구역 갯수 확인
    for x in range(N):
        for y in range(M):
            if lab[x][y] == 0:
                count += 1

    # 바이러스 퍼지기 전으로 연구실 복구
    for v_idx in restore:
        lab[v_idx[0]][v_idx[1]] = 0

    return count

# N : 세로 크기, M : 가로 크기
N, M = map(int,input().split())

# 델타 (상 하 좌 우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 연구소 정보
lab = [list(map(int,input().split())) for _ in range(N)]

wall = 0

safe_area = 0

build_wall(lab, 0)

print(safe_area)
