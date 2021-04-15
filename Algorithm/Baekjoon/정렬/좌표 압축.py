import sys

N = int(input())

data = list(map(int,sys.stdin.readline().split()))

sort_num = sorted(list(set(data)))

for num in data:
    print(sort_num.index(num), end=' ')