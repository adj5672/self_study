def DFS(idx, prob):

    global max_prob

    # 일을 모두 분배한 경우
    if idx == N:
        if prob > max_prob:
            max_prob = prob
        return
    
    # 이미 확률이 0 인 경우 return
    # 나머지가 전부 100% 라도 최대 확률을 넘지 못하면 return
    if prob == 0 or prob * 100 ** (N-idx) < max_prob:
        return
    
    for i in range(N):
        if not visited[i]:
            if arr[idx][i] != 0:
                visited[i] = 1
                DFS(idx+1, prob * arr[idx][i])
                visited[i] = 0

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # N : 직원의 수, 일의 갯수
    N = int(input())

    # arr : 일을 성공할 확률
    arr = [list(map(int,input().split())) for _ in range(N)]
    
    # 주어진 일을 모두 성공할 최대 확률
    max_prob = 0

    # 방문배열
    visited = [0 for _ in range(N)]

    DFS(0, 1)
    max_prob = round(max_prob / (100 ** (N-1)), 6)

    # 출력
    print('#{} {:.6f}'.format(test_case, max_prob))