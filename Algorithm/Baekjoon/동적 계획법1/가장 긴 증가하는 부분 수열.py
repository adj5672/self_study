N = int(input())

data = list(map(int,input().split()))

result = []

for idx in range(N):
    for j in range(len(result)):
        seq = [x for x in result[j]]
        if seq[0] < data[idx]:
            seq[0] = data[idx]
            seq[1] = result[j][1] + 1
            result.append(seq)
    result.append([data[idx], 1])

result.sort(key=lambda x: x[1])
print(result[-1][1])
