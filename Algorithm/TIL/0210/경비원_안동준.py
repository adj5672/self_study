# X : 블록의 가로길이, Y : 블록의 세로길이
X, Y = map(int,input().split())
# 상점의 갯수
stores_number = int(input())
# 상점의 위치 2차원 배열
stores = []
for _ in range(stores_number):
    stores.append(list(map(int,input().split())))
# 동근의 위치
Dg = list(map(int,input().split()))
# 총 움직인 거리
total_move = 0

for store in stores:

    # 같은 방향 경계에 있으면
    if Dg[0] == store[0]:
        total_move += abs(Dg[1]-store[1])

    # 둘다 X축 위에 있을 때
    elif Dg[0] in [1, 2] and store[0] in [1, 2]:
        d1 = Y + Dg[1] + store[1]
        d2 = 2*(X+Y) - d1
        total_move = total_move + d1 if d1 < d2 else total_move + d2
    # 둘다 Y축 위에 있을 때
    elif Dg[0] in [3, 4] and store[0] in [3, 4]:
        d1 = X + Dg[1] + store[1]
        d2 = 2*(X+Y) - d1
        total_move = total_move + d1 if d1 < d2 else total_move + d2

    # 동근 북쪽, 상점 서쪽
    elif Dg[0] == 1 and store[0] == 3:
        total_move += Dg[1] + store[1]
    # 동근 북쪽, 상점 동쪽
    elif Dg[0] == 1 and store[0] == 4:
        total_move += (X-Dg[1]) + store[1]
    # 동근 남쪽, 상점 서쪽
    elif Dg[0] == 2 and store[0] == 3:
        total_move += Dg[1] + (Y-store[1])
    # 동근 남쪽, 상점 동쪽
    elif Dg[0] == 2 and store[0] == 4:
        total_move += (X-Dg[1]) + (Y-store[1])
        

    # 상점 북쪽, 동근 서쪽
    elif store[0] == 1 and Dg[0] == 3:
        total_move += Dg[1] + store[1]
    # 상점 북쪽, 동근 동쪽
    elif store[0] == 1 and Dg[0] == 4:
        total_move += (X - store[1]) + Dg[1]
    # 상점 남쪽, 동근 서쪽
    elif store[0] == 2 and Dg[0] == 3:
        total_move += store[1] + (Y - Dg[1])
    # 상점 남쪽, 동근 동쪽
    elif store[0] == 2 and Dg[0] == 4:
        total_move += (X - store[1]) + (Y - Dg[1])

# 출력
print(total_move)