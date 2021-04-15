def DFS(idx, num, remain):

    copy_operator = [o for o in operator]

    if [copy_operator, remain] in visited:
        return

    if remain == 0:
        if num < value[0]:
            value[0] = num
        if num > value[1]:
            value[1] = num
        return

    visited.append([copy_operator, remain])

    for i in range(4):
        if operators[i]:
            if i == 0:
                operator.append(i)
                operators[i] -= 1
                DFS(idx+1, num + nums[idx+1], remain - 1)
                operators[i] += 1
                operator.pop()
            if i == 1:
                operator.append(i)
                operators[i] -= 1
                DFS(idx + 1, num - nums[idx + 1], remain - 1)
                operators[i] += 1
                operator.pop()
            if i == 2:
                operator.append(i)
                operators[i] -= 1
                DFS(idx + 1, num * nums[idx + 1], remain - 1)
                operators[i] += 1
                operator.pop()
            if i == 3:
                operator.append(i)
                operators[i] -= 1
                if num >= 0:
                    DFS(idx + 1, num // nums[idx + 1], remain - 1)
                else:
                    DFS(idx + 1, -(-num // nums[idx + 1]), remain - 1)
                operators[i] += 1
                operator.pop()


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

DFS(0, nums[0], N-1)

# 출력
print(value[1], value[0])