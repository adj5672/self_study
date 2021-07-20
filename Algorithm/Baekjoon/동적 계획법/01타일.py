def tile(n):

    memo = [1, 2]

    if n <= 2:
        return memo[n-1]
    for _ in range(n-2):
        memo[0], memo[1] = memo[1] % 15746, (memo[0] + memo[1]) % 15746
    return memo[-1]

N = int(input())

print(tile(N))