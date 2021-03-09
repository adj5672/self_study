# n * n 색종이 부착 가능성 여부 검사
# (i,j) 가 색종이의 왼쪽 상단
def paper(n,i,j):
    # (i,j) 를 왼쪽 상단으로 하여 색종이를 붙일 수 없다면 return False
    for x in range(n):
        for y in range(n):
            if not (0 <= i + x < 10) or not (0 <= j + y < 10) or arr[i+x][j+y] == 0:
                return False
    # 가능하다면 색종이를 붙이고
    else:
        for x in range(n):
            for y in range(n):
                arr[i+x][j+y] = 0
        # return True
        return True

# 종이
arr = []
for _ in range(10):
    arr.append(list(map(int,input().split())))

# 붙여야 할 색종이 갯수
count = 0

# P * P 색종이 부터
for P in range(5, 0, -1):
    use = 0
    stop = 0
    for Y in range(10):
        if stop:
            break
        for X in range(10):
            if arr[X][Y] == 1 and paper(P, X, Y):
                count += 1
                use += 1
            if use >= 5:
                stop = 1
                break

for check in range(10):
    if any(arr[check]):
        result = -1
        break
else:
    result = count

# 출력
print(result)