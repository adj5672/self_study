N = int(input())

data = [input() for _ in range(N)]
data = list(set(data))

data.sort(key= lambda x: (len(x), x))

for word in data:
    print(word)