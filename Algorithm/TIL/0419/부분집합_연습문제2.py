data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def DFS(idx, total, n):

    # 부분집합이 완성된 경우
    if idx == n:
        if total == 10:
            result_subset = [x for x in subset]
            result.append(result_subset)
        return

    # 이미 합이 10을 넘었을 경우 return
    if total > 10:
        return
    
    # idx 번째 숫자가 부분집합에 포함된 경우
    subset.append(data[idx])
    DFS(idx+1, total + data[idx], n)
    subset.pop()
    # idx 번째 숫자가 부분집합에 포함되지 않은 경우
    DFS(idx+1, total, n)

# subset : 부분집합, result : 결과값, N : 집합의 크기
subset = []
result = []
N = len(data)

DFS(0, 0, N)

# 출력
print(result)