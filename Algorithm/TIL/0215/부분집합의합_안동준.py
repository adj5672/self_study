# 데이터 및 데이터의 길이
data = [-7,-3,-2,5,8]
N = len(data)

# 결과값
result = []

for i in range(1 << N):
    # 각 부분집합을 담을 list와 그 부분집합의 합
    subset, subset_sum = [], 0
    # 부분집합 구하기
    for j in range(N):
        if i & (1 << j):
            subset.append(data[j])
    # 부분집합 원소들의 합 구하기
    for num in subset:
        subset_sum += num
    # 만약 합이 0이라면 그 부분집합을 result에 추가
    if subset_sum == 0:
        result.append(subset)

# 출력
print(result)