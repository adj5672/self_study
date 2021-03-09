def DFS(idx, color, value):

    global min_fee

    if value > min_fee:
        return

    if idx == N:
        if min_fee > value:
            min_fee = value
            return

    else:
        for i in range(3):
            if i != color:
                DFS(idx+1, i, value + house[idx][color])      
    

N = int(input())

min_fee = N * 1000

house = [list(map(int,input().split())) for _ in range(N)]

for i in range(3):
    DFS(0,i,0)

print(min_fee)

# 시간초과

# [마지막 집 빨간색, 마지막 집 초록색, 마지막 집 파란색]