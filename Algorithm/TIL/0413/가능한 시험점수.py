# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # N : 문제 갯수
    N = int(input())
    # 각 문제의 배점
    scores = list(map(int,input().split()))

    # 가능한 점수들 (최대 100문제, 각 문제 당 최대 배점 100)
    result = [0 for _ in range(10001)]
    result[0] = 1

    # 각 점수마다
    for score in scores:
        # 방문 배열
        visited = [0 for _ in range(10001)]
        for i in range(10001):
            # 해당 문제를 제외한 문제들에서 얻은 점수 결과를 찾기
            if result[i] and not visited[i]:
                # 해당 문제를 맞췄을 때의 총점 정보가 존재하지 않는다면 추가
                if not result[i + score]:
                    result[i + score] = 1
                    visited[i + score] = 1

    # 가능한 총점 갯수
    count = 0
    for i in range(10001):
        if result[i]:
            count += 1

    # 출력
    print('#{} {}'.format(test_case, count))