N, K = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
data.sort(key=lambda x: (x[0], x[1]), reverse=True)

result = [0 for _ in range(K+1)]

while data:
    cur = data.pop()
    w, v = cur[0], cur[1]
    if w <= K:
        for i in range(K, -1, -1):
            if result[i]:
                if i + w <= K and result[i + w] < result[i] + v:
                    result[i + w] = result[i] + v
        result[w] = v

print(max(result))
