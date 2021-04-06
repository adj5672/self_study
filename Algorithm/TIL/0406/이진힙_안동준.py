# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # 노드의 갯수
    N = int(input())

    # 노드 값 정보
    data = list(map(int,input().split()))

    # tree 구성 [현재 노드의 저장값]
    tree = [0 for i in range(N+1)]

    # 1번 노드에 첫번째 값 저장
    tree[1] = data[0]

    # 2번 노드부터 순서대로 값을 저장하는데
    # 부모 노드와 계속해서 크기 비교하며 더 큰 값 저장
    for idx in range(2, N+1):
        num = data[idx-1]
        if num < tree[idx//2]:
            while idx != 0:
                if num < tree[idx//2]:
                    n = tree[idx//2]
                    tree[idx] = n
                    tree[idx//2] = num
                    idx = idx//2
                else:
                    break
        else:
            tree[idx] = data[idx-1]

    # 조상 노드에 저장된 값 합산
    total = 0
    while N != 0:
        N = N // 2
        total += tree[N]

    # 출력
    print('#{} {}'.format(test_case, total))