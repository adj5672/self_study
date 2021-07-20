n = int(input())
data = [1, 1]
while len(data) <= n:
    data.append(data[-1] + data[-2])
print(data[n] % 10007)
