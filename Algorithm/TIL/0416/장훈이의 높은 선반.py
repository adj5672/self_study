def DFS(idx, height, remain):
    
    # 모든 점원이 사용된 경우
    if idx == N:
        if height >= B:
            result.add(height-B)
        return
    
    # 중간에 이미 선반의 높이를 넘어선 경우
    if height >= B:
        result.add(height-B)
        return
    
    # 남은 직원들이 모두 탑을 쌓아도 선반에 닿지 않는 경우
    if remain + height < B:
        return

    # idx 번째 점원이 탑을 쌓은 경우
    DFS(idx+1, height + H[idx], remain - H[idx])
    # idx 번째 점원이 탑을 쌓지 않은 경우
    DFS(idx+1, height, remain - H[idx])


# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # N : 점원의 수, B : 선반의 높이, H : 점원들의 키 정보
    N, B = map(int,input().split())
    H = list(map(int,input().split()))

    # S : 점원들의 키의 합
    S = sum(H)

    # 가능한 높이와 선반의 높이의 차
    result = set()

    DFS(0, 0, S)

    # 출력
    print('#{} {}'.format(test_case, min(result)))