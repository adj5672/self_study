def russia(idx,sub_sum):

    global min_value

    if sub_sum > N:
        return

    if idx == 3:
        if sub_sum == N:
            cnt = 0

            st = sel[0]
            st2 = st + sel[1]
            st3 = st2 + sel[2]

            for i in flag[:st]:
                for j in i:
                    if j != 'W':
                        cnt += 1

            for i in flag[st:st2]:
                for j in i:
                    if j != 'B':
                        cnt += 1

            for i in flag[st2:st3]:
                for j in i:
                    if j != 'R':
                        cnt += 1

            if cnt < min_value:
                min_value = cnt

        return

    for i in range(1, N-1):
        sel[idx] = i
        russia(idx+1, sub_sum + i)


# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # N : 행의 갯수, M : 열의 갯수
    N, M = map(int,input().split())
    # min_value : 칠해야 하는 칸의 최소 갯수
    min_value = N * M

    # 현재 국기
    flag = [list(input()) for _ in range(N)]

    # 각 색깔의 줄 수
    sel = [0 for _ in range(3)]
    
    # idx, 중간 합
    russia(0, 0)

    # 출력
    print('#{} {}'.format(test_case, min_value))

# 중복 조합 경우를 구하는데 DPS 사용하니 메모리 제한을 넘기고
# BFS를 사용하니 시간초과가 나옴..
