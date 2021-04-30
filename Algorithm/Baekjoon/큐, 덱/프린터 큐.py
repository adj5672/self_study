import sys
from collections import deque

T = int(input())

for test_case in range(T):
    N, target = map(int,input().split())
    important = list(map(int,input().split()))
    data = deque()
    for d in enumerate(important):
        data.append(d)

    count = 0
    while True:
        paper = data.popleft()
        for d in data:
            if paper[1] < d[1]:
                data.append(paper)
                break
        else:
            count += 1
            if paper[0] == target:
                break

    print(count)