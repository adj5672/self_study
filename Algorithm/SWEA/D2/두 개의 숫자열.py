# test_case 갯수
T = int(input())

for test_case in range(1,T+1):

    # 입력값 받아오기
    N, M = map(int,input().split())
    Ai = list(map(int,input().split()))
    Bi = list(map(int,input().split()))

    # Ai를 길이가 더 짧은 list로 설정
    if N > M:
        Ai, Bi = Bi, Ai
        N, M = M, N

    max_total = 0
    # Bi 의 i번째 인덱스와 Ai의 0번째 인덱스부터 계산
    for i in range(0,M-N+1):
        sum_total = 0
        # Ai의 길이가 더 짧으므로 Ai의 길이만큼 반복
        for j in range(0,N):
            sum_total += Ai[j] * Bi[j+i]
        # 최댓값인지 확인후 최댓값이면 값 저장
        if sum_total > max_total:
            max_total = sum_total
    # 출력
    print('#{} {}'.format(test_case,max_total))
