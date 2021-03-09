# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    D, L, N = map(int,input().split())
    damage = 0
    for n in range(N):
        damage += D * (1 + n * L * 0.01)

    print('#{} {}'.format(test_case,int(damage)))