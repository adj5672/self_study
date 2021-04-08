# 집과 치킨집 사이의 거리
def dist(home, chicken):
    return abs(home[0] - chicken[0]) + abs(home[1] - chicken[1])

# N : 도시의 크기, M : 최대 치킨집 갯수
N, M = map(int,input().split())

# 도시 정보
city = [list(map(int,input().split())) for _ in range(N)]

# 집과 치킨집의 위치정보
home, chicken = [], []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

# 최소의 치킨거리
min_total = 2 * N * len(home)

# 남길 치킨집의 index M개 뽑기 (비트 마스킹을 사용한 부분집합 구하기)
idx = list(range(len(chicken)))
n = len(idx)
for i in range(1 << n):
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(idx[j])
    # 크기가 M인 부분집합의 경우
    if len(subset) == M:
        total = 0
        # 각 집마다 치킨 거리를 계산
        for h in home:
            c_dist = []
            for i in subset:
                c_dist.append(dist(h,chicken[i]))
            total += min(c_dist)
        # 도시의 치킨 거리의 최솟값과 비교
        if min_total > total:
            min_total = total

# 출력
print(min_total)