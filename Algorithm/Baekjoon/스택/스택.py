import sys
from collections import deque

N = int(input())
stack = deque()

for _ in range(N):
    order_data = sys.stdin.readline()[:-1].split()
    order = order_data[0]

    if order == 'push':
        stack.append(order_data[1])

    elif order == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif order == 'size':
        print(len(stack))

    elif order == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    elif order == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)