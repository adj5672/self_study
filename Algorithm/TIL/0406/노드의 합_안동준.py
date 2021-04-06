# 후위 순회
def post_order(node):

    if node <= N:
        post_order(tree[node][0])
        post_order(tree[node][2])
        # 만약 왼쪽 자식이 존재한다면 루트에 값 더하기
        if tree[node][0] <= N:
            tree[node][1] += tree[tree[node][0]][1]
        # 만약 오른쪽 자식이 존재한다면 루트에 값 더하기
        if tree[node][2] <= N:
            tree[node][1] += tree[tree[node][2]][1]

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # N : 노드의 갯수, M : 잎 노드의 갯수, L : 출력할 노드 번호
    N, M, L = map(int,input().split())

    # tree 구성 [왼쪽 자식 노드 번호, 현재 노드의 저장값, 오른쪽 자식 노드 번호]
    tree = [[2*i, 0, 2*i+1] for i in range(N+1)]

    # 잎 노드에 값 저장
    for _ in range(M):
        n, v = map(int,input().split())
        tree[n][1] = v
    
    # 함수 실행
    post_order(1)

    # 출력
    print('#{} {}'.format(test_case, tree[L][1]))