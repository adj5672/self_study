N = int(input())

data = [list(map(int,input().split())) for _ in range(N)]

data.sort(key=lambda x: (x[0], x[1]))

for x in data:
    print(' '.join(list(map(str,x))))