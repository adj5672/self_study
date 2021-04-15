# N : 자연수 갯수, M : 조합의 갯수
N, M = map(int,input().split())

nums = list(range(1,N+1))
comb = [0] * M

# 중복 순열 (n H r)
def H(idx, remain, n):

    # r개를 뽑은 경우 출력
    if remain == 0:
        print(' '.join(list(map(str,comb))))
        return

    # 뽑아야 할 갯수가 남은 갯수보다 많은 경우 return
    if n - idx < remain:
        return

    for i in range(N):
        if idx == 0:
            comb[idx] = nums[i]
            H(idx+1, remain-1, n)
        elif nums[i] >= comb[idx-1]: 
            comb[idx] = nums[i]
            H(idx+1, remain-1, n)

H(0, M, N)