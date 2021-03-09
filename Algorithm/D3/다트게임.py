# 원점으로부터의 거리
def dist(x, y):
    return ((x ** 2) + (y ** 2)) ** 0.5

# test_case 갯수
T = int(input())
score = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]

for test_case in range(1,T+1):
    N = int(input())
    total_score = 0

    # 각 다트의 원점으로부터의 거리 구하기
    shoot = []
    for _ in range(N):
        x, y = map(int,input().split())
        shoot.append(dist(x, y))

    # 각 다트 점수 구하기
    for dart in shoot:
        for s in range(len(score)):
            if dart <= score[s]:
                total_score += 10 - s
                break
        
    # 출력
    print('#{} {}'.format(test_case, total_score))