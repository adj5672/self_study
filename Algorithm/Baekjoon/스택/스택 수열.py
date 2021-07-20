n = int(input())
data = [int(input()) for _ in range(n)]
num, idx = 1, 0
stack = []
result = ''

for _ in range(n):
    if data[idx] >= num:
        for i in range(num, data[idx]+1):
            result += '+' + '\n'
            stack.append(i)
        result += '-' + '\n'
        stack.pop()
        num = data[idx] + 1
        idx += 1
    else:
        if stack[-1] != data[idx]:
            result = 'NO'
            break
        else:
            result += '-' + '\n'
            stack.pop()
            idx += 1

print(result)
