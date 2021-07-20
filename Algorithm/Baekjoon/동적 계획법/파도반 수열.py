def tri(n):

    if n <= 10:
        return memo[n-1]

    elif n > len(memo):
        memo.append(tri(n-1) + tri(n-5))

    return memo[n - 1]

T = int(input())

memo = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for _ in range(T):
    N = int(input())

    print(tri(N))