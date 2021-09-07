n = int(input())
data = list(map(int, input().split()))
data.sort()
x = int(input())
cnt = 0

if n == 1 and data[0] == x:
    cnt = 1
else:
    i, j = 0, n-1
    while i != j:
        if data[i] + data[j] == x:
            cnt += 1
            i += 1
        elif data[i] + data[j] > x:
            j -= 1
        else:
            i += 1

print(cnt)
