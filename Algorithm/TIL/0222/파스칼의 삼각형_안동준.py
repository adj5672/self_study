# test_case 갯수
T = int(input())

for test_case in range(1,T+1):

    # N : 줄의 갯수
    N = int(input())
    # 결과값에 파스칼 삼각형 첫번째 줄 [1]을 append
    result = [[1]]

    # 두 번째 줄부터 N번 째 줄까지 (각 i+1 번째 줄)
    for i in range(1,N):

        # 두 번째 줄이면 [1, 1]을 결과값에 append
        if i == 1:
            result.append([1, 1])

        # 그 외 i+1 번째 줄이면
        else:
            # 첫번째 숫자 1 입력
            pascal = [1]
            # j번 숫자는 i 번째 줄의 j-1 번 숫자와 j 번 숫자의 합
            for j in range(len(result[i-1]) - 1):
                pascal.append(result[i-1][j] + result[i-1][j+1])
            # 마지막 숫자 1 추가
            pascal.append(1)
            # 결과값에 파스칼의 삼각형 i+1 번째 줄 append
            result.append(pascal)
            
    # 출력
    print(f'#{test_case}')
    for pascal in result:
        print(' '.join(map(str,pascal)))