N = int(input())

data = list(map(int,input().split()))
result = [0] * N
result[0] = data[0]

for i in range(1, N):
    result[i] = max(result[i-1]+data[i], data[i])

print(max(result))