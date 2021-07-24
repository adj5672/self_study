N, M = map(int, input().split())
data = list(map(int, input().split()))
result = 0

for i in range(N):
    total = 0
    for j in range(i, N):
        total += data[j]
        if total == M:
            result += 1
            break
        elif total > M:
            break

print(result)
