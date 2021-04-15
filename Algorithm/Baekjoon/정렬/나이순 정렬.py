N = int(input())

data = [input().split() + [i] for i in range(N)]

data.sort(key=lambda x: (int(x[0]), x[2]))

for i in data:
    print(i[0], i[1])