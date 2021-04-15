# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # N : 컨테이너 갯수, M : 트럭의 갯수
    N, M = map(int,input().split())

    # W : 화물의 무게, T : 트럭의 적재 용량
    W = list(map(int,input().split()))
    T = list(map(int,input().split()))

    # total : 총 화물 운반량
    total = 0

    # 트럭의 적재 용량 및 화물의 무게를 오름차순으로 정렬
    T.sort()
    W.sort()

    # 트럭이 없거나 화물이 없어질 떄까지
    while W and T:
        # truck : 적재 용량이 가장 큰 트럭
        truck = T[-1]
        # W[0] : 가장 가벼운 화물
        # 만약 옮길 수 있는 화물이 존재한다면
        if W[0] <= truck:
            # 화물 중 현재 트럭이 운반 가능한 가장 무거운 화물 찾기
            max_w = 0
            for i in range(len(W)):
                if (W[i] <= truck) and (W[i] >= W[max_w]):
                    max_w = i
            # 총 운반량 추가 및 옮겨진 화물, 옮긴 트럭 제거
            total += W.pop(max_w)
            T.pop()
        # 없다면 while문 종료
        else:
            break

    # 출력
    print('#{} {}'.format(test_case, total))
