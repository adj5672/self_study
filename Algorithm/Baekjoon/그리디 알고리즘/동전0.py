N, K = map(int,input().split())

coin = [int(input()) for _ in range(N)]

count = 0
for idx in range(-1,-len(coin)-1,-1):
    if K // coin[idx] != 0:
        count += K // coin[idx]
        K = K % coin[idx]

print(count)