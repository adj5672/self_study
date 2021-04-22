def Find_set(x):
    if p[x] == x:
        return x
    else:
        return Find_set(p[x])

def Union(x, y):
    p[Find_set(y)] = Find_set(x)

# test_case 갯수
T = int(input())

for test_case in range(1, T+1):
    # V : 마지막 노드 번호, E : 간선의 갯수
    V, E = map(int,input().split())
    
    # 간선 정보 (가중치 기준 오름차순 정렬)
    data = []
    for _ in range(E):
        data.append(list(map(int,input().split())))
    data.sort(key=lambda x: x[2])

    # Make_set
    p = [i for i in range(V+1)]
    
    # edge : 선택된 간선의 갯수, idx : 간선 정보 인덱스, total : 가중치의 합
    edge, idx, total = 0, 0, 0
    # 선택된 간선의 갯수가 정점의 갯수 - 1 이 될 때까지
    while edge < V:
        u, v, w = data[idx][0], data[idx][1], data[idx][2]
        # cycle 이 형성이 안될 때
        if Find_set(u) != Find_set(v):
            edge += 1
            total += w
            Union(u, v)
        idx += 1
    
    # 출력
    print('#{} {}'.format(test_case, total))