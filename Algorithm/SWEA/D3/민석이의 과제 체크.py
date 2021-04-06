T = int(input())

for tc in range(1,T+1):
    N, F = map(int,input().split())
    student = list(range(1,N+1))
    Fs = list(map(int,input().split()))
    for f in Fs:
        student.remove(f)
    print('#{} {}'.format(tc, ' '.join(map(str,student))))