# 방법 1
# 한 번 이동할 때마다, 주어진 배열의 맨 앞 숫자를 pop 하여 맨 뒤로 append

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # N : 숫자의 갯수, M : 이동 횟수
    N, M = map(int,input().split())
    
    # 주어진 숫자 배열
    data = list(map(int,input().split()))

    # 배열의 맨 앞 숫자를 pop 하여 맨 뒤에 append 한다. 이를 M번 반복
    for _ in range(M):
        data.append(data.pop(0))

    # 배열 맨 앞 숫자 출력
    print('#{} {}'.format(test_case, data[0]))

##############################################################################

# 방법 2
# 배열을 이동시키지 않고 배열의 M 번째 값을 출력하는 방법
# N 번 이동 시 원래 배열로 돌아오므로 M이 N보다 큰 경우 M % N 번째 값을 출력한다.

# test_case 갯수
T = int(input())

for test_case in range(1, T + 1):
    # N : 숫자의 갯수, M : 이동 횟수
    N, M = map(int, input().split())

    # 주어진 숫자 배열
    data = list(map(int, input().split()))

    # data의 M % N 번째 값 출력
    print('#{} {}'.format(test_case, data[M % N]))