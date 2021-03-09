# test_case 갯수
T = int(input())

for test_case in range(1,T+1):

    # N : 화덕의 크기, M : 피자의 갯수
    N, M = map(int,input().split())

    # M 개의 피자에 뿌려진 치즈의 양
    cheeze = list(map(int,input().split()))
    
    # 피자의 번호 (0번 부터 시작) 및 화덕
    pizza = [p for p in range(M)]
    oven = []
    
    # 처음 피자 N개를 화덕에 넣는다. (각 피자의 번호를 append 한다.)
    for _ in range(N):
        oven.append(pizza.pop(0))

    # 화덕에 남은 피자가 한 개일 때까지
    while len(oven) != 1:

        # 화덕이 1 바퀴 돌 때, 각 피자마다
        for _ in range(len(oven)):

            # 1번 위치에 놓인 피자의 치즈가 녹는다.
            cheeze[oven[0]] = cheeze[oven[0]] // 2

            # 만약 치즈가 다 녹았다면
            if cheeze[oven[0]] == 0:
                # 화덕에서 피자를 꺼낸다.
                oven.pop(0)
                # 그리고 아직 구워야 할 피자가 있다면 화덕에 넣는다.
                try:
                    oven.append(pizza.pop(0))
                except:
                    pass

            # 만약 치즈가 다 녹지 않았다면
            else:
                # 다시 화덕의 맨 뒤로 이동한다.
                oven.append(oven.pop(0))

            # 만약 화덕에 피자가 한 개만 남았다면 종료
            if len(oven) == 1:
                break

    # 최종적으로 남은 피자의 번호는 oven[0] + 1
    result = oven.pop(0) + 1

    # 출력
    print('#{} {}'.format(test_case, result))