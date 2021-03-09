# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # 레이저 위치를 r로 replace
    data = input()
    data = data.replace('()', 'r')
    bar = 0
    result = 0

    # 나눠지는 막대기 갯수 구하기
    for i in data:
        # 만약 레이저라면 쌓여있는 막대기 자르기 (잘려진 막대기의 왼쪽 부분 갯수를 result에 추가)
        if i == 'r':
            result += bar
        # 막대기의 시작점이라면 막대기 갯수 1개 추가
        elif i == '(':
            bar += 1
        # 막대기의 종료점이라면 막대기 갯수 1개 감소 및 다 잘려진 막대기의 가장 오른쪽 부분 result에 추가
        else:
            bar -= 1
            result += 1

    # 출력
    print('#{} {}'.format(test_case, result))