'''
1,2,3,4,5,6,7,8,9,10의 powerset 중 원소의 합이 10인 부분집합을 구하시오
'''

# 집합의 크기
N = 10
# selector
sel = [0 for _ in range(N)]

# 주어진 집합
data = [i for i in range(1,11)]
# 결과값
result = []

def powerset(idx):
    if idx == N:
        # 부분집합 만들기
        subset = []
        # select 된 원소를 부분집합에 넣기
        for i in range(N):
            if sel[i]:
                subset.append(data[i])
        # 만약 부분집합 원소의 합이 10이면 결과값에 append
        if sum(subset) == 10:
            result.append(subset)

    else:
        # idx+1 이 부분집합 원소에 포함이 안 된 경우
        sel[idx] = 0
        powerset(idx+1)
        # idx+1 이 부분집합 원소에 포함 된 경우
        sel[idx] = 1
        powerset(idx+1)

# 함수 호출
powerset(0)

# 출력
print(result)