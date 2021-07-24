T = int(input())
memo = [1, 2, 4]
while len(memo) < 11:
    memo.append(memo[-1] + memo[-2] + memo[-3])

for _ in range(T):
    n = int(input())
    print(memo[n-1])
