# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    code = input()
    result = []
    # code를 거꾸로 순회
    for i in range(-1,-len(code)-1,-1):
        if code[i] == 'b':
            result.append('d')
        elif code[i] == 'd':
            result.append('b')
        elif code[i] == 'p':
            result.append('q')
        elif code[i] == 'q':
            result.append('p')
    
    # 출력
    print('#{} {}'.format(test_case,''.join(result)))