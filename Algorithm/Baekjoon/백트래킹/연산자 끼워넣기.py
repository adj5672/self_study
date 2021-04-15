def DFS(idx, num, remain):

    copy_operator = [o for o in operator]

    if [operator, remain] in visited:
        return

    if remain == 0:
        result.append(copy_operator)
        return

    visited.append([copy_operator, remain])

    for i in range(4):
        # if operators[i]:
        #     operator.append(i)
        #     operators[i] = operators[i] - 1
        #     DFS(idx+1, num, remain-1)
        #     operators[i] = operators[i] + 1
        #     operator.pop()
        if operators[i]:
            if i == 0:
                operators[i] = operators[i] - 1
                DFS(idx+1, )

# 숫자의 갯수
N = int(input())

# 피연산자들
nums = list(map(int,input().split()))

# 각 연산자의 갯수
operators = list(map(int,input().split()))
operator = []

visited = []
result = []

# 최솟값, 최댓값
value = [10 ** 9, -1 * 10 ** 9]

DFS(0, 0, N-1)
