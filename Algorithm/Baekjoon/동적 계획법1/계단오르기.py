N = int(input())
stairs = [0]
for _ in range(N):
    stairs.append(int(input()))
if N < 3:
    print(sum(stairs))
else:
    arr = [[x, x] for x in stairs]
    for i in range(2, N+1):
       arr[i][1] = arr[i][1] + arr[i-1][0]
       arr[i][0] = max([arr[i][0] + arr[i-2][0], arr[i][0] + arr[i-2][1]])
    print(max(arr[-1]))