# 종이를 채우는 재귀 함수 (n : 채워야 하는 영역의 길이) (memoization)
def paper(n):
    # 만약 memo가 False라면
    if not memo[n]:
        # 점화식으로 부터 memo값 구하기
        memo[n] = paper(n-10) + 2 * paper(n-20)
    # 그 외엔 memo return
    return memo[n]

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    # memo 만들기
    memo = [0 for _ in range(301)]
    # 점화식 초기값 설정
    memo[0], memo[10] = 1, 1
    # 재귀함수 실행
    paper(N)

    # 출력
    print('#{} {}'.format(test_case,memo[N]))