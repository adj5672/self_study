def DFS(idx):

    if idx == M:
        print(' '.join(map(str,sel)))

    else:
        for i in range(N):
            sel[idx] = numbers[i]
            DFS(idx+1)

N, M = map(int,input().split())

numbers = [i for i in range(1,N+1)]

sel = [0] * M

DFS(0)