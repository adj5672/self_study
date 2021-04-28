import sys

K = int(input())

arr = [0] * K
top = -1

for _ in range(K):
    num = int(sys.stdin.readline())
    if num:
        top += 1
        arr[top] = num
    else:
        top -= 1

result = 0
for i in range(top+1):
    result += arr[i]

print(result)