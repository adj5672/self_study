# 중위순회 함수
def in_order(node):

    global num
    
    # N 이하의 노드만..
    if node <= N:
        in_order(tree[node][0])
        num += 1
        tree[node][1] = num
        in_order(tree[node][2])

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    # tree 구성 [왼쪽 자식 노드 번호, 현재 노드의 저장값, 오른쪽 자식 노드 번호]
    tree = [[2*i, 0, 2*i+1] for i in range(N+1)]

    num = 0

    # 함수 실행
    in_order(1)

    # 출력
    print('#{} {} {}'.format(test_case, tree[1][1], tree[N//2][1]))