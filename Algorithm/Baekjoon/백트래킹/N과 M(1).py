def DFS(idx):

    if idx == M:
        print(' '.join(map(str,sel)))

    else:
        for i in range(N):
            if visited[i] == 0: 
                sel[idx] = numbers[i]
                visited[i] = 1
                DFS(idx+1)
                visited[i] = 0

N, M = map(int,input().split())

numbers = [i for i in range(1,N+1)]

visited = [0 for _ in range(N)]

sel = [0] * M

DFS(0)