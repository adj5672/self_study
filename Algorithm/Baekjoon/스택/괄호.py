import sys

T = int(input())

for tc in range(1, T+1):

    data = list(sys.stdin.readline())[:-1]
    n = len(data)
    stack = [0] * n
    top = -1
    result = 'YES'

    for i in range(n):
        if data[i] == '(':
            top += 1
            try:
                stack[top] = 1
            except:
                result = 'NO'
                break
        else:
            top -= 1
            if top < -1:
                result = 'NO'
                break

    if top != -1:
        result = 'NO'

    print(result)