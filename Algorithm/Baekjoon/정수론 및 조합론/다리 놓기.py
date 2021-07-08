T = int(input())

memo = [1]
i = 1
while i < 30:
    memo.append(memo[-1] * i)
    i += 1

for _ in range(T):
    N, M = map(int, input().split())
    if N < M:
        N, M = M, N
    print(int(memo[N] / (memo[M] * memo[N-M])))
    