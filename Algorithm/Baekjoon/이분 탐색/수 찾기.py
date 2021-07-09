def bin_search(s, e, target):
    
    m = (s + e) // 2
    if s > e:
        return 0
    if A[m] == target:
        return 1
    
    if target < A[m]:
        return bin_search(s, m-1, target)
    else:
        return bin_search(m+1, e, target)

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
X = list(map(int, input().split()))

for x in X:
    print(bin_search(0, N-1, x))