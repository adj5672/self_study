# test_case 갯수 10개
for _ in range(10):
    # test_case 번호
    test_case = int(input())
    # 8개의 data
    data = list(map(int,input().split()))
    # cycle이 True인 동안 while문 반복
    cycle = True

    while cycle:
        # while문 한 바퀴에 사이클 1번이 실행된다.
        for i in range(1,6):
            # 만약 사이클을 돌던 중 0 보다 작아지는 경우 프로그램을 종료한다.
            if data[0] - i <= 0:
                data.pop(0)
                data.append(0)
                cycle = False
                break
            # 그 외의 경우에는 i 만큼 감소시킨 후 맨 뒤로 이동 시킨다.
            else:
                n = data.pop(0)
                data.append(n - i)

    # 출력
    print('#{} {}'.format(test_case, ' '.join(map(str,data))))
