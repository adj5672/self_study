import sys
from collections import deque

N = int(input())
queue = deque()

for _ in range(N):
    order_data = sys.stdin.readline()[:-1].split()
    order = order_data[0]

    if order == 'push':
        queue.append(order_data[1])

    elif order == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif order == 'size':
        print(len(queue))

    elif order == 'empty':
        if queue:
            print(0)
        else:
            print(1)

    elif order == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif order == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)