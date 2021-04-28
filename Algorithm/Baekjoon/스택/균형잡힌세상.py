import sys

while True:
    data = sys.stdin.readline()[:-1]
    if data == '.':
        break

    n = len(data)
    stack = [0] * n
    top = -1
    arr = ['(', ')', '[', ']']
    result = 'yes'
    for i in range(n):
        if data[i] not in arr:
            continue

        if data[i] == '(':
            top += 1
            stack[top] = '('

        elif data[i] == ')':
            try:
                if stack[top] != '(':
                    result = 'no'
                    break
                else:
                    top -= 1
            except:
                result = 'no'
                break

        elif data[i] == '[':
            top += 1
            stack[top] = '['

        elif data[i] == ']':
            try:
                if stack[top] != '[':
                    result = 'no'
                    break
                else:
                    top -= 1
            except:
                result = 'no'
                break

    if top != -1:
        result = 'no'

    print(result)