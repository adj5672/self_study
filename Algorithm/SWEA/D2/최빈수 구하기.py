# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    case_number = int(input())

    # 각 점수 갯수를 담을 배열
    count = [0 for _ in range(101)]
    # 학생들 점수 data
    scores = list(map(int,input().split()))
    
    # 점수 count 하기
    for score in scores:
        count[score] += 1
    
    # 최빈수 구하기
    max_count, max_score = 0, 0
    for score, student in enumerate(count):
        if student >= max_count:
            max_count = student
            max_score = score

    # 출력
    print('#{} {}'.format(case_number, max_score))
