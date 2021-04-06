# 후위순회
def post_order(node):

    # 해당 정점의 값이 숫자라면 형 변환
    if tree[node][1] not in operator:
        tree[node][1] = float(tree[node][1])
        
    # 해당 정점의 값이 연산자라면
    else:
        left_c, right_c = int(tree[node][0]), int(tree[node][2])
        post_order(left_c)
        post_order(right_c)
        # 연산 후 루트에 연산 결과 저장
        if tree[node][1] == '+':
            tree[node][1] = tree[left_c][1] + tree[right_c][1]
        elif tree[node][1] == '-':
            tree[node][1] = tree[left_c][1] - tree[right_c][1]
        elif tree[node][1] == '*':
            tree[node][1] = tree[left_c][1] * tree[right_c][1]
        elif tree[node][1] == '/':
            tree[node][1] = tree[left_c][1] / tree[right_c][1]

# test_case 갯수
T = 10

for test_case in range(1,T+1):
    # N : 정점의 갯수
    N = int(input())

    # tree 구성 [왼쪽 자식 번호, 현재 노드 저장값, 오른쪽 자식 번호]
    tree = [[0] * 3 for _ in range(N+1)]

    # 연산자 배열
    operator = ['+', '-', '*', '/']

    # 각 정점 정보
    for _ in range(N):
        data = input().split()
        # 해당 정점에 값 저장
        tree[int(data[0])][1] = data[1]
        # 왼쪽 자식 번호 저장
        try:
            tree[int(data[0])][0] = data[2]
        except:
            pass
        # 오른쪽 자식 번호 저장
        try:
            tree[int(data[0])][2] = data[3]
        except:
            pass
    
    # 함수 실행
    post_order(1)

    # 출력
    print('#{} {}'.format(test_case, int(tree[1][1])))
