N = int(input())
pre_data = [int(input())]

for _ in range(N-1):
    data = list(map(int,input().split()))
    for i in range(len(data)):
        if i == 0:
            data[i] = data[i] + pre_data[i]
        elif i == len(data)-1:
            data[i] = data[i] + pre_data[i-1]
        else:
            data[i] = max(pre_data[i-1] + data[i], pre_data[i] + data[i])
    pre_data = data

print(max(data))

