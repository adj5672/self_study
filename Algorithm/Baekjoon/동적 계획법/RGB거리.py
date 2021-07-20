import sys

N = int(input())

RGB = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

result = [0, 0 ,0]

for i in range(N):
    red = min(result[1] + RGB[i][0], result[2] + RGB[i][0])
    green = min(result[0] + RGB[i][1], result[2] + RGB[i][1])
    blue = min(result[0] + RGB[i][2], result[1] + RGB[i][2])

    result = [red, green, blue]

print(min(result))