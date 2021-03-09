T = int(input())

for test_case in range(1,T+1):
    D, A, B, F = map(int,input().split())
    move = D * F / (A + B)
    print('#{} {}'.format(test_case, move))