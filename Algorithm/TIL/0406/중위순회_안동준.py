# 중위순회 함수
def in_order(node):
    if tree[node][1]:
        in_order(tree[node][0])
        result.append(tree[node][1])
        in_order(tree[node][2])

# test_case 갯수
T = 10

for test_case in range(1,T+1):
    # 노드의 갯수
    V = int(input())

    # tree 구성 [왼쪽 자식, 현재 정점 알파벳, 오른쪽 자식]
    tree = [[0] * 3 for _ in range(V+1)]

    for _ in range(V):
        # data : 각 정점의 정보
        data = input().split()

        # data[0] : 정점 번호, data[1] : 정점 알파벳
        tree[int(data[0])][1] = data[1]

        # 왼쪽 자식이 존재하면 정보 저장
        try:
            tree[int(data[0])][0] = int(data[2])
        except:
            pass
        # 오른쪽 자식이 존재하면 정보 저장
        try:
            tree[int(data[0])][2] = int(data[3])
        except:
            pass

    # result : 처리 결과
    result = []
    # 함수 실행
    in_order(1)

    # 결과 출력
    print('#{} {}'.format(test_case, ''.join(result)))
