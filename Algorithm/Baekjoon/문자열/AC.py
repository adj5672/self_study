from collections import deque


def AC(order, n, data):
    if not n:
        if 'D' in order:
            return 'error'
        else:
            return '[]'
    reverse = False
    data = deque(data[1:-1].split(','))
    for o in order:
        if o == 'R':
            reverse = not reverse
        elif o == 'D':
            if reverse:
                try:
                    data.pop()
                except:
                    return 'error'
            else:
                try:
                    data.popleft()
                except:
                    return 'error'
    if not reverse:
        return '[' + ','.join(data) + ']'
    else:
        return '[' + ','.join(reversed(data)) + ']'


N = int(input())

for _ in range(N):
    order = input()
    n = int(input())
    data = input()
    print(AC(order, n, data))
