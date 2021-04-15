import sys

# 숫자의 갯수
N = int(input())

# 산술평균
average = 0

# 중앙값 및 범위
arr = []

# 최빈값
count = [0 for _ in range(8001)]

for _ in range(N):
    # 정수 받아오기
    n = int(sys.stdin.readline())
    
    # 산술평균
    average += n / N

    # 중앙값 및 범위
    arr.append(n)

    # 최빈값
    count[n+4000] += 1

arr.sort()
# 산술평균
print(round(average))
# 중앙값
print(arr[N // 2])
# 최빈값
max_count = max(count)
result = []
for idx, count in enumerate(count):
    if count == max_count:
        result.append(idx)
if len(result) == 1:
    print(result[0] - 4000)
else:
    print(result[1] - 4000)
# 범위
print(arr[-1] - arr[0])