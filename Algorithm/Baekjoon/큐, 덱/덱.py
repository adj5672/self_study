import sys
from collections import deque

N = int(input())
queue = deque()

for _ in range(N):
    data = sys.stdin.readline()[:-1].split()
    order = data[0]

    if order == 'push_back':
        queue.append(data[1])

    elif order == 'push_front':
        queue.appendleft(data[1])

    elif order == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif order == 'pop_back':
        if queue:
            print(queue.pop())
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

    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)