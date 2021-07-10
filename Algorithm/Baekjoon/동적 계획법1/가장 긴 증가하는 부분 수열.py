N = int(input())
A = list(map(int, input().split()))
cnt = [0 for _ in range(N)]

if N == 1:
    cnt[0] = 1
else:
    cnt[-1] = 1
    for i in range(N-2, -1, -1):
        if A[i] >= max(A[i+1:]):
            cnt[i] = 1
        else:
            for j in range(i+1, N):
                if A[i] < A[j] and cnt[i] <= cnt[j]:
                    cnt[i] = cnt[j] + 1

print(max(cnt))