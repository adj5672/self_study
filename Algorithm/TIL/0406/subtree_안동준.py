# 중위 순회 함수
def in_order(node):

    global count
    
    if node:
        in_order(left[node])
        count += 1
        in_order(right[node])    

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # E : 간선의 갯수, N : 루트
    E, N = map(int,input().split())

    # left : 왼쪽 자식, right : 오른쪽 자식
    left = [0 for _ in range(E+2)]
    right = [0 for _ in range(E+2)]

    # 간선 정보
    data = list(map(int,input().split()))
    for i in range(E):
        p, c = data[2*i], data[2*i+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
    
    # 노드의 갯수
    count = 0

    # 함수 실행
    in_order(N)

    # 출력
    print('#{} {}'.format(test_case, count))