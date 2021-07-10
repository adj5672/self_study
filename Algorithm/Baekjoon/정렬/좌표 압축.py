N = int(input())
X = list(map(int, input().split()))
order = list(set(X))
order.sort()
key = {}
for idx, num in enumerate(order):
    key[num] = idx
print(' '.join(list(map(str, list(map(lambda x: key[x], X))))))