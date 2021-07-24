def gcd(a, b):
    return a if not b else gcd(b, a % b)


M, N = map(int, input().split())
g = gcd(M, N)
l = int(M * N / g)
print(g)
print(l)
