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
    # N : 출석 번호, M : 신청서 갯수
    N, M = map(int,input().split())
    
    # Make_set : 각 사람이 지목한 사람의 번호
    p = [i for i in range(N+1)]

    # 신청서 정보
    data = list(map(int,input().split()))
    for i in range(M):
        u, v = data[2*i], data[2*i+1]
        Union(u, v)

    # 각 조의 조장(p[x] = x)이 몇 명인지 count
    count = 0
    for j in range(1, N+1):
        if p[j] == j:
            count += 1

    # 출력
    print('#{} {}'.format(test_case, count))