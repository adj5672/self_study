# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # 사람 수
    N = int(input())

    # 각 개인의 소득
    people = list(map(int,input().split()))

    # 평균소득
    total = 0
    for person in people:
        total += person
    average = total / N
    
    # 평균 이하 소득 count
    count = 0
    for person in people:
        if person <= average:
            count += 1

    # 출력
    print('#{} {}'.format(test_case, count))