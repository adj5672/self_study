import sys
input = sys.stdin.readline

N = int(input())
count = [0 for _ in range(10001)]
for _ in range(N):
    count[int(input())] += 1
for i in range(10001):
    for j in range(count[i]):
        print(i)