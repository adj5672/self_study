def Find_set(x):
    if p[x] == x:
        return x
    return Find_set(p[x])

def Union(x, y):
    p[Find_set(y)] = Find_set(x)

# test_case 갯수
T = int(input())

for test_case in range(1, T+1):
    # N : 마을 사람의 수, M : 관계의 수
    N, M = map(int,input().split())

    # Make_set
    p = [i for i in range(N+1)]

    # 관계로부터 무리 만들기
    for _ in range(M):
        u, v = map(int,input().split())
        Union(u, v)

    # 무리 숫자 세기
    count = 0
    for i in range(1, N+1):
        if p[i] == i:
            count += 1

    # 출력
    print('#{} {}'.format(test_case, count))