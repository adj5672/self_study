# 명령의 수
N = int(input())

stack = []

for _ in range(N):
    order = input().split()

    if order[0] == 'push':
        stack.append(int(order[1]))

    elif order[0] == 'pop':
        try:
            print(stack.pop())
        except:
            print(-1)

    elif order[0] == 'size':
        print(len(stack))

    elif order[0] == 'empty':
        if stack:
            print(1)
        else:
            print(0)

    elif order[0] == 'top':
        try:
            print(stack[-1])
        except:
            print(-1)